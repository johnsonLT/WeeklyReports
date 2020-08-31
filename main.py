# -*- coding: utf-8 -*-
# @Time : 2020/8/12 19:47
# @Author : johnsonLT
# @Site : 
# @File : main.py
# @Software: PyCharm

import sys
import os
from copy import copy
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
        print(self.directory)
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
       summaryWorkPath = self.directory + '/' + self.summaryReportPath
       print(summaryWorkPath)
       self.summaryReportWork = openpyxl.load_workbook(summaryWorkPath)
       self.memberName = []
       for reportWork in self.personReportPathList:
           curReportPath = self.directory + '/' + reportWork
           memberName = self.getStrBetweenSymbol(reportWork, '_', '.')
           self.memberName.append(memberName)
           print(self.memberName)
           self.replace_xls(curReportPath, summaryWorkPath, memberName)

           # self.personReportWork
    def getStrBetweenSymbol(self, txt, c_start, c_end):
        start = txt.find(c_start)
        if start >= 0:
            start += len(c_start)
            end = txt.find(c_end, start)
            if end >= 0:
                return txt[start:end].strip()

    # src_file是源xlsx文件，tag_file是目标xlsx文件，sheet_name是目标xlsx里的新sheet名称
    def replace_xls(self, src_file, tag_file, sheet_name):
        print("Start sheet %s copy from %s to %s" % (sheet_name, src_file, tag_file))
        wb = openpyxl.load_workbook(src_file)
        wb2 = openpyxl.load_workbook(tag_file)

        ws = wb.get_sheet_by_name(wb.get_sheet_names()[0])

        ws2 = wb2.create_sheet(sheet_name.decode('utf-8'))

        max_row = ws.max_row  # 最大行数
        max_column = ws.max_column  # 最大列数

        wm = zip(ws.merged_cells)  # 开始处理合并单元格
        if len(wm) > 0:
            for i in range(0, len(wm)):
                cell2 = str(wm[i]).replace('(<MergeCell ', '').replace('>,)', '')
                print("MergeCell : %s" % cell2)
                ws2.merge_cells(cell2)

        for m in range(1, max_row + 1):
            ws2.row_dimensions[m].height = ws.row_dimensions[m].height
            for n in range(1, 1 + max_column):
                if n < 27:
                    c = chr(n + 64).upper()  # ASCII字符,chr(65)='A'
                else:
                    if n < 677:
                        c = chr(divmod(n, 26)[0] + 64) + chr(divmod(n, 26)[1] + 64)
                    else:
                        c = chr(divmod(n, 676)[0] + 64) + chr(divmod(divmod(n, 676)[1], 26)[0] + 64) + chr(
                            divmod(divmod(n, 676)[1], 26)[1] + 64)
                i = '%s%d' % (c, m)  # 单元格编号
                if m == 1:
                    #				 print("Modify column %s width from %d to %d" % (n, ws2.column_dimensions[c].width ,ws.column_dimensions[c].width))
                    ws2.column_dimensions[c].width = ws.column_dimensions[c].width
                try:
                    getattr(ws.cell(row=m, column=c), "value")
                    cell1 = ws[i]  # 获取data单元格数据
                    ws2[i].value = cell1.value  # 赋值到ws2单元格
                    if cell1.has_style:  # 拷贝格式
                        ws2[i].font = copy(cell1.font)
                        ws2[i].border = copy(cell1.border)
                        ws2[i].fill = copy(cell1.fill)
                        ws2[i].number_format = copy(cell1.number_format)
                        ws2[i].protection = copy(cell1.protection)
                        ws2[i].alignment = copy(cell1.alignment)
                except AttributeError as e:
                    print("cell(%s) is %s" % (i, e))
                    continue

        wb2.save(tag_file)

        wb2.close()
        wb.close()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = AgentUI()
   main.show()
   sys.exit(app.exec())
