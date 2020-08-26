# -*- coding: utf-8 -*-
# @Time : 2020/8/12 19:47
# @Author : johnsonLT
# @Site : 
# @File : main.py
# @Software: PyCharm

import sys, os
import pandas as pd
import WeeklyReports
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore


class AgentUI(QMainWindow, WeeklyReports.Ui_MainWindow):
    def __init__(self):
        super(AgentUI, self).__init__()
        self.initUI()
    def initUI(self):
        self.setupUi(self)  # 向主窗口添加控件
        self.btn_select.clicked.connect(self.on_linePathShow)
        self.btn_select.clicked.connect(self.on_filesList)
        self.btn_generate.clicked.connect(self.on_generateReports)
    def on_linePathShow(self):
        self.directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.line_path.setText(self.directory)
    def on_filesList(self):
        self.filesList = os.listdir(self.directory)
        self.listWidget_filelist.addItems(self.filesList)
    def on_generateReports(self):

        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AgentUI()
    main.show()
    sys.exit(app.exec())
