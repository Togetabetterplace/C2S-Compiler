import re
# 一些判断函数和字符分割函数放在同级文件function.py中
import sys
import os

sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
from other.function import if_num, if_name, have_name, printf, get_word

# 运算符表
y_list = {"+", "-", "*", "/", "<", "<=", ">", ">=", "=", "==", "!=", "^", ",", "&", "&&", "|", "||", "%", "~", "<<",
          ">>", "!"}
# 分隔符表
f_list = {";", "(", ")", "[", "]", "{", "}", ".", ":", "\"", "#", "\'", "\\", "?"}
# 关键字表
k_list = {
    "auto", "break", "case", "const", "continue", "default", "do", "else", "enum", "extern",
    "for", "goto", "if", "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "volatile", "while", "printf", "else", "for"
}

Cmp = ["<", ">", "==", "!=", ">=", "<="]

Type = {"int", "float", "char", "double", "void", "long", "unsigned", "string"}
type_flag = ""
# 括号配对判断
kuo_cp = {'{': '}', '[': ']', '(': ')'}


# 词法分析器输出对象
# 成员变量：输出的单词表，源代码中的分隔符表,运算符表,变量表,关键字表
# 一个方法，将源代码字符切割并存入对应表中
# 对象创建实例需要传入filename参数，默认为test.c
class Word_List:
    def __init__(self, filename = 'test.c'):
        self.word_list = []  # 输出单词列表
        self.separator_list = []  # 分隔符
        self.operator_list = []  # 运算符
        self.name_list = []  # 变量
        self.key_word_table = []  # 关键字
        self.string_list = []
        self.flag = True  # 源代码是否正确标识

        # get_word函数将源代码切割
        gword = get_word(filename)
        # print("-------------------------------------------------")
        # print("词语表")
        # print(gword)
        # print("-------------------------------------------------")
        self.Create_Table(gword)

    # 创建各个表
    def Create_Table(self, in_words):
        name_id = 0
        kuo_list = []  # 存储括号并判断是否完整匹配
        char_flag = False
        str_flag = False
        string_list = []
        strings = ""
        chars = ""
        for word in in_words:
            w = word['word']
            line = word['line']
            if w == '"':  # 判定是否为字符串
                if not str_flag:
                    str_flag = True
                else:
                    str_flag = False
                    self.word_list.append({'line': line, 'type': 'TEXT', 'word': strings})
                    self.string_list.append(strings)
                    strings = ""
                # self.word_list.append({'line':line, 'type':w, 'word':w})
                continue
            # 判断是否为字符串
            if str_flag:
                strings += w
                continue
            if w == "'":
                if not char_flag:
                    char_flag = True
                else:
                    char_flag = False
                    self.word_list.append({'line': line, 'type': 'CHAR', 'word': chars})
                    chars = ""
                continue
            if char_flag:
                chars += w
                continue
            # 判断为关键字
            if w in k_list:
                self.key_word_table.append({'line': line, 'type': 'keyword', 'word': w})
                self.word_list.append({'line': line, 'type': w, 'word': w})
            elif w in Cmp:
                self.word_list.append({'line': line, 'type': "Cmp", 'word': w})
            # 判断为关键字
            elif w in Type:
                type_flag= w
                self.key_word_table.append({'line': line, 'type': 'type', 'word': w})
                self.word_list.append({'line': line, 'type': 'type', 'word': w})
            # 判断为运算符
            elif w in y_list:
                self.operator_list.append({'line': line, 'type': 'operator', 'word': w})
                self.word_list.append({'line': line, 'type': w, 'word': w})
            # 判断为分隔符
            elif w in f_list:
                if w in kuo_cp.values() or w in kuo_cp.keys():
                    # 左括号入栈
                    if w in kuo_cp.keys():
                        kuo_list.append({'kuo': w, 'line': line})
                    # 右括号判断是否匹配并出栈
                    elif w == kuo_cp[kuo_list[-1]['kuo']]:
                        kuo_list.pop()
                    else:
                        print("Error：在第" + str(line) + "行的' " + w + " '无法匹配")
                        self.flag = False
                        return
                self.separator_list.append({'line': line, 'type': 'separator', 'word': w})
                self.word_list.append({'line': line, 'type': w, 'word': w})
            # 其他字符处理
            else:
                if if_num(w):
                    self.word_list.append({'line': line, 'type': 'number', 'word': w})
                # 如果是变量名要判断是否已经存在且被声明
                elif if_name(w):
                    if have_name(self.name_list, w):
                        self.word_list.append({'line': line, 'type': 'name', 'word': w, 'id': name_id})
                    else:
                        for i, j in enumerate(in_words):  # 找到索引，并检查索引前一个字段是不是声明关键字
                            if j == word and in_words[i-1]["word"] != "int" and in_words[i-1]["word"] != "char" and in_words[i-1]["word"] != "float":
                                print(" Error：在第" + str(line) + "行的变量名 " + w + "未声明")
                                self.flag = False
                                return
                        self.name_list.append({'line': line, 'id': name_id, 'word': 0.0, 'name': w, 'flag': type_flag})
                        self.word_list.append({'line': line, 'type': 'name', 'word': w, 'id': name_id})
                        name_id += 1
                else:
                    print(
                        "Error：在第" + str(line) + "行的变量名' " + w + " '不可识别")
                    self.flag = False
                    return
        if kuo_list:
            print("Error：在第" + str(kuo_list[0]['line']) + "行的' " + kuo_list[0][
                'kuo'] + " '无法匹配")
            self.flag = False
            return


if __name__ == '__main__':
    filename = input("请输入要编译的.c文件:")
    if filename == '':
        filename = 'test/test1.c'
    w_list = Word_List(filename)
    if w_list.flag:
        print("-------------------------------------------------")

        print("\n输出词语表如下")
        printf(w_list.word_list)
        print("\n\n输出变量表如下\n")
        printf(w_list.name_list)
        print("-------------------------------------------------")

