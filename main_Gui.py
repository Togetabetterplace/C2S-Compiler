import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QLineEdit, QLabel, QMessageBox
from asm import to_asm
from exe import to_exe
from generate import creat_mcode
from get_Ptable import grammars, show_tables
from LR import analysis
import os
from lexer import Word_List

head = """
--------------------------+
Welcome to C2S-C语言编译器|
--------------------------+
"""

phelp = """+-------------------------------------------------+
按钮操作即可
- Mcode为四元式
- Grammar为语法表                           
+-------------------------------------------------+
"""


class PCCCompilerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.selected_file = ""

    def initUI(self):
        self.setWindowTitle("C2S Compiler")

        self.command_input = QLineEdit(self)
        self.command_input.setPlaceholderText("Enter command here")

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        self.button_help = QPushButton("Help", self)
        self.button_help.clicked.connect(self.show_help)

        self.button_select_file = QPushButton("Select File", self)
        self.button_select_file.clicked.connect(self.select_file)

        self.button_generate_asm = QPushButton("Generate ASM (AT&T)", self)
        self.button_generate_asm.clicked.connect(self.generate_asm)

        self.button_generate_exe = QPushButton("Generate EXE file", self)
        self.button_generate_exe.clicked.connect(self.generate_exe)

        self.button_show_mcode = QPushButton("Show MCode", self)
        self.button_show_mcode.clicked.connect(self.show_mcode)

        self.button_show_syntax_tree = QPushButton("Show Syntax Tree", self)
        self.button_show_syntax_tree.clicked.connect(self.show_syntax_tree)

        self.button_show_lexical_analysis = QPushButton(
            "Show Lexical Analysis", self)
        self.button_show_lexical_analysis.clicked.connect(
            self.show_lexical_analysis)

        self.button_show_predict_table = QPushButton(
            "Show Predict Table", self)
        self.button_show_predict_table.clicked.connect(self.show_predict_table)

        self.button_show_grammar = QPushButton("Show Grammar", self)
        self.button_show_grammar.clicked.connect(self.show_grammar)

        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Command Output"))
        left_layout.addWidget(self.text_edit)

        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Enter Command"))
        right_layout.addWidget(self.command_input)
        right_layout.addWidget(self.button_select_file)
        right_layout.addWidget(self.button_help)
        right_layout.addWidget(self.button_generate_asm)
        right_layout.addWidget(self.button_generate_exe)
        right_layout.addWidget(self.button_show_mcode)
        right_layout.addWidget(self.button_show_syntax_tree)
        right_layout.addWidget(self.button_show_lexical_analysis)
        right_layout.addWidget(self.button_show_predict_table)
        right_layout.addWidget(self.button_show_grammar)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def show_help(self):
        self.text_edit.append(phelp)

    def select_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select C File")
        if filename:
            self.selected_file = filename
            self.text_edit.append(f"Selected file: {self.selected_file}")

    def execute_command(self, command):
        self.text_edit.append(f">>> C2S >>> {command}")
        os.system(command)

    def generate_asm(self):
        if self.selected_file:
            try:
                to_asm(self.selected_file)
                name = self.selected_file.split("/")[-1]
                self.text_edit.append(
                    f"\t编译成功，生成汇编代码 {self.selected_file[:-1]}s")
            except Exception as e:
                self.text_edit.append(f"\t编译失败: {e}")
        else:
            self.text_edit.append("\tNo file selected")


    def generate_exe(self):
        if self.select_file:
            try:
                to_exe(self.selected_file)
                name = self.selected_file.split("/")[-1]
                self.text_edit.append(
                    f"\t编译成功，生成可执行文件 {self.selected_file[:-1]}exe")
            except Exception as e:
                self.text_edit.append(f"\t编译失败: {e}")
        else:
            self.text_edit.append("\tNo file selected")
    
    def show_mcode(self):
        if self.selected_file:
            mid = creat_mcode(self.selected_file)['mid_code']
            for m in mid:
                self.text_edit.append(str(m))
        else:
            self.text_edit.append("\tNo file selected")

    def show_syntax_tree(self):
        if self.selected_file:
            w_list = Word_List(self.selected_file)
            word_table = w_list.word_list
            root = analysis(word_table, True)
            if root[0]:
                reply = QMessageBox.question(
                    self, 'Print Syntax Tree', "是否打印语法树(左边为父节点，右边为子节点)?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.text_edit.append(str(root[1]))
                    self.text_edit.append("\n\n语法树打印完成")
        else:
            self.text_edit.append("\tNo file selected")

    def show_lexical_analysis(self):
        if self.selected_file:
            w_list = Word_List(self.selected_file)
            if w_list.flag:
                self.text_edit.append("\nlexical_analysis结果如下")
                for w in w_list.word_list:
                    self.text_edit.append(str(w))
        else:
            self.text_edit.append("\tNo file selected")

    def show_predict_table(self):
        first_table, follow_table, predict_table = show_tables()
        self.text_edit.append("\nfirst集合:\n")
        for k in first_table:
            self.text_edit.append(k)
            self.text_edit.append(str(first_table[k]))
        self.text_edit.append("\nfollow集合:\n")
        for k in follow_table:
            self.text_edit.append(k)
            self.text_edit.append(str(follow_table[k]))
        # print(first_table)
        self.text_edit.append("\n预测表:\n")
        for k in predict_table:
            self.text_edit.append(k)
            self.text_edit.append(str(predict_table[k]))
        # self.text_edit.append

    def show_grammar(self):
        for g in grammars:
            self.text_edit.append(f"{g}: {grammars[g]}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = PCCCompilerGUI()
    gui.resize(900,700)
    gui.show()
    gui.text_edit.append(head)
    sys.exit(app.exec_())
