"""
中间代码转汇编代码

"""
from generate import creat_mcode
from other.function import if_num

global_head = """
;PCC compiler master------------------------------------------------
;-------------------------------------------------------------------
"""

code_head = """
\tpush    rbp
    mov     eax, 8064
    call    ___chkstk_ms
    sub     rsp, rax
    lea     rbp, 128[rsp]
    call    __main
"""

code_footer = """
\tmov\teax,0
	add\trsp, 8064
\tpop\trbp
	ret
"""

"""
两个全局变量
STR 字符串计数
re 存储汇编代码
"""
STR = 0
re = ""

"""
agrs函数，解析变量，转为汇编语言可识别的变量
n：传入的变量，name变量名表
其中带[]的为数组变量，将会进行特殊的寻址处理
"""


def args(n, name):
    global re
    if n in name:
        return "DWORD PTR " + name[n][0] + "[rbp]"
    elif "[]" in str(n):
        ags = n.split("[]")
        if if_num(ags[1]):
            if name[ags[0]][1] == "char":
                return "DWORD PTR " + str(int(name[ags[0]][0]) - int(ags[1])) + "[rbp]"
            elif name[ags[0]][1] == "int":
                return "DWORD PTR " + str(int(name[ags[0]][0]) - int(ags[1]) * 4) + "[rbp]"
        else:
            re += "\tmov\t" + args(ags[1], name) + ", eax\n\tcltq\n"
            if name[ags[0]][1] == "char":
                return "DWORD PTR " + name[ags[0]][0] + "[rbp+rax*1]"
            elif name[ags[0]][1] == "int":
                return "DWORD PTR " + name[ags[0]][0] + "[rbp+rax*4]"

    elif "T" in str(n):
        return n + "[rip]"
    elif if_num(str(n)):
        return str(n)

    else:
        return n


"""
变量初始化，给每个变量初始化地址。
对于数组给予相应长度地址空间
返回值[re, len]
re为变量名地址对照表， len为需要数据栈的高度（这里我规定为12的倍数）
"""


def init_data(name_list, arrs):
    re = {}
    i = 0
    for n in name_list:
        if n['name'] != "main":
            if n['flag'] == "int":
                i += 4
                re[n['name']] = [str(i), "int"]
            elif n['flag'] == 'char':
                i += 1
                re[n['name']] = [str(i), "char"]
    for a in arrs:
        if arrs[a][1] == "int":
            i += int(arrs[a][0]) * 4
            re[a] = [str(i), "int"]
    return [re, (int(i / 12) + 1) * 12]


"""
字符串初始化
"""


def init_string(strings):
    re = ""
    for i in range(0, len(strings)):
        re += ".LC" + str(i) + ":\n\t.string \"" + strings[i] + "\"\n"
    return re


"""
汇编代码生成
传入参数：
    1. midcode中间代码（四元式）
    2. name变量地址参照表
可解析的汇编语句有
    1. 赋值语句（op，=）
    2. 四则运算（op，+-*/)
    3. 跳转语句（op，j）
    4. 输出语句（op，print）
"""


def generate_code(mid_code, name):
    global re
    re = ""
    for m in mid_code:
        # args = arg(m, name)
        a1 = args(m.arg1, name)
        a2 = args(m.arg2, name)
        r = args(m.re, name)
        if m.op == "=":

            if m.re in name and name[m.re][1] == "char":
                re += "\tmov\t" + r + ", " + str(ord(m.arg1)) + "\n"
            elif m.arg1 in name or "T" in m.arg1 or "[]" in m.arg1:
                re += "\tmov\t" + "ecx, " + a1 + "\n"
                re += "\tmov\t" + r + ", ecx\n"
            else:
                re += "\tmov\t" + r + ", " + a1 + "\n"
        elif m.op == "code_block":
            re += "." + m.re + ":\n"
            continue

        elif "j" in m.op:
            if m.op == "j":
                re += "\tjmp\t." + m.re + "\n"
            else:
                re += "\tmov\t" + "eax, " + a1 + "\n"
                re += "\tcmp\t" + "eax, " + a2 + "\n"
                if ">" in m.op:
                    re += "\tjg\t." + m.re + "\n"
                elif "<" in m.op:
                    re += "\tje\t." + m.re + "\n"
                elif "=" in m.op:
                    re += "\tje\t." + m.re + "\n"

        elif m.op in "+-":
            re += "\tmov\t" + "edx, " + a1 + "\n"
            re += "\tmov\t" + "eax, " + a2 + "\n"
            if m.op == "+":
                re += "\tadd\teax, edx\n"
            else:
                re += "\tsub\teax, edx\n"
            re += "\tmov\t" + r + ", eax\n"

        elif m.op in "*/":
            if m.arg1 in name:
                re += "\tmov\t" + "eax, " + a2 + "\n"
                re += "\timul\t" + "eax, " + a1 + "\n"
                re += "\tmov\t" + r + ", eax\n"
            elif m.arg2 in name and m.arg1 not in name:
                re += "\tmov\t" + "eax, " + a2 + "\n"
                re += "\timul\t" + "eax, " + a1 + "\n"
                re += "\tmov\t" + r + ", eax\n"
            elif m.arg2 not in name and m.arg1 not in name:
                num = int(m.arg2) * int(m.arg1)
                re += "\tmov\t" + r + ", " + str(num) + "\n"

        elif m.op == "print":
            global STR
            if m.arg1 != "-1":
                if m.arg1 in name and name[m.arg1][1] == "char":
                    re += "\tmovsb\teax, " + a1 + "\n"
                else:
                    re += "\tmov\teax, " + a1 + "\n"
            if m.arg2 != "-1":
                if m.arg2 in name and name[m.arg2][1] == "char":
                    re += "\tmovsb\tedx, " + a2 + "\n"
                else:
                    re += "\tmovl\tedx, " + a2 + "\n"
            if m.re != "-1":
                if m.re in name and name[m.re][1] == "char":
                    re += "\tmovsb\tecx, " + r + "\n"
                else:
                    re += "\tmov\tecx, " + r + "\n"
            re += "\tmov\tesi, eax\n" + "\tleaq\t.LC" + str(STR) + "[rip], rdi\n"
            STR += 1
            re += "\tmov\t01h, eax\n\tcall\tprintf@PLT\n"

    return re


"""
字符串拼接函数
将生成的临时变量，汇编代码，头部，结束部分等一些内容拼接在一起
传入参数：
    1. tmp 临时变量（其实在代码里作为全局变量）
    2. strs 字符串变量
    3. code 主函数汇编代码
    4. subq 数据栈高度
"""


def connect(tmp, strs, code, subq):
    data = ""
    re = "main:"+code_head + "\tsubq\t" +  "rsp, "+str(subq) +"\n" + code + code_footer
    return re


"""
入口函数
生成汇编代码.s文件
"""


def to_asmi(filename):
    global STR
    STR = 0
    mid_result = creat_mcode(filename)
    mid_code = mid_result['mid_code']
    name_list = mid_result['name_list']
    tmp = mid_result['tmp']
    strings = mid_result['strings']
    arrs = mid_result['arrs']
    name = init_data(name_list, arrs)
    string_list = init_string(strings)
    asm = generate_code(mid_code, name[0])
    result = connect(tmp, string_list, asm, name[1])
    re_asm = open(filename[:-1] + "asm", "w").write(result)


if __name__ == "__main__":
    to_asmi("./test/test1.c")
