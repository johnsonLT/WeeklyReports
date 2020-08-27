# -*- coding: utf-8 -*-
# @Time : 2020/8/12 19:47
# @Author : johnsonLT
# @Site : 
# @File : main.py
# @Software: PyCharm

import sys, os
import pandas as pd
import openpyxl
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
    '''
    slot function, connect to the btn_select clicked signal.
    '''
    def on_linePathShow(self):
        self.directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.line_path.setText(self.directory)
    '''
    slot function, connect to the btn_select clicked signal.
    Description: get the summary report path, and put everyone report path into a list.
    '''
    def on_filesList(self):
        self.filesList = os.listdir(self.directory)
        self.listWidget_filelist.addItems(self.filesList)
        self.personReportPathList = []
        for report in self.filesList:
            if report.find('_') == -1 :
                self.summaryReportPath = report
                print(self.summaryReportPath)
            else:
                self.personReportPathList.append(report)
    '''
    slot function, connect to the btn_generate clicked signal.  
    '''
    def on_generateReports(self):
       self.summaryReportWork = openpyxl.load_workbook(self.summaryReportPath)
       for reportWork in self.personReportPathList:
           self.personReportWork = openpyxl.load_workbook(reportWork)
           self.getStrBetweenSymbol(reportWork, '_', '.')

           # self.personReportWork
    def getStrBetweenSymbol(self, txt, c_start, c_end):
        start = txt.find(c_start)
        if start >= 0:
            start += len(c_start)
            end = txt.find(c_end, start)
            if end >= 0:
                return txt[start:end].strip()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = AgentUI()
   main.show()
   sys.exit(app.exec())
