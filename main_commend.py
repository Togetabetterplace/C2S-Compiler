"""
PCC编译器入口函数

"""
from to_asm import to_asm
from generate import creat_mcode
from get_Ptable import grammars
from LR import analysis
import os
from lexer import Word_List

head = """
:::Welcome to PCC master——Ｃ语言编译器
:::使用帮助：pcc -h
"""

phelp = """+-------------------------------------------------+
|\tpcc -s [filename]\t生成汇编源码(AT&T)           
|\tpcc -m [filename]\t查看生成的四元式        
|\tpcc -t [filename]\t查看语法树生成过程   
|\tpcc -l [filename]\t查看词法分析        
|\tpcc -p \t查看预测分析表                   
|\tpcc -g \t查看语法推导                     
|\tquit\t退出                            
+-------------------------------------------------+
"""


def begin():
    print(head)
    while True:
        print(":::PCC >>> ", end="")  # 字符串分割获取命令要求和文件路径
        s = input()
        slist = s.split()
        if len(slist) == 0:
            continue
        if slist[0] != "pcc" or len(slist) > 3:
            try:
                os.system(s)
            except:
                print("输入错误，请重新输入")
                print(phelp)
                # print("-----------------------------")
            continue
        if slist[0] == "exit":
            print("Thanks for using！")
            return
        elif slist[1] == "-h":
            print(phelp)
        elif slist[1] == "-m":
            mid = creat_mcode(slist[2])['mid_code']
            for m in mid:
                print(m)
        elif slist[1] == "-s":
            try:
                to_asm(slist[2])
                name = slist[2].split("/")[-1]
                print("\t编译成功，生成汇编代码" + slist[2][:-1] + "s")
            except:
                print("\t编译失败")
        elif slist[1] == "-t":
            w_list = Word_List(slist[2])
            word_table = w_list.word_list
            root = analysis(word_table, True)
            if root[0]:
                print("\n\n是否打印语法树(左边为父节点，右边为子节点)？\n\t1.打印 \n\t2.任意键退出")
                if input() == "1":
                    print(root[1])
                    print("\n\n语法树打印完成！")
        elif slist[1] == "-l":
            w_list = Word_List(slist[2])
            if w_list.flag:
                print("\n输出字符串如下")
                for w in w_list.word_list:
                    print(w)
        elif slist[1] == "-p":
            os.system("python predict_table.py")
        elif slist[1] == "-g":
            for g in grammars:
                print(g, grammars[g])


if __name__ == "__main__":
    begin()
