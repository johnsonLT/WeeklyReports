# -*- coding: utf-8 -*-
# @Time : 2020/8/12 19:47
# @Author : johnsonLT
# @Site : 
# @File : main.py
# @Software: PyCharm

import sys
import os
import threading
from copy import copy
import pandas as pd
import openpyxl
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment
import WeeklyReports
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, Color

'''
global list
'''
#成员名称
memberList = []

'''
excel class, contain excel attribute and handle 
'''
class reportExcel():
    def __init__(self, excelID):
        print("#init reportExcel:%d", excelID)
        pass
    # src_file是源xlsx文件，tag_file是目标xlsx文件，sheet_name是目标xlsx里的新sheet名称
    # noinspection PyMethodMayBeStatic
    def replace_xls(self, src_file, tag_file, sheet_name):
        print("Start sheet %s copy from %s to %s" % (sheet_name, src_file, tag_file))
        wbSrc = openpyxl.load_workbook(src_file)
        if os.path.exists(src_file):
            wbTag = openpyxl.load_workbook(tag_file)
        else:
            wbTag = openpyxl.Workbook()
        if sheet_name in wbSrc.sheetnames:
            wsSrc = wbSrc[sheet_name]
        else:
            wsSrc = wbSrc.active
            wsSrc.title = sheet_name

        if sheet_name in wbTag.sheetnames:
            wsTag = wbTag[sheet_name]
        else:
            wsTag = wbTag.create_sheet(title=sheet_name)
        #处理合并单元格
        self.handleMergedCells(wsSrc, wsTag)
        #处理单个单元格
        self.handleSingleCell(wsSrc, wsTag)
        wbTag.save(filename=tag_file)

    #处理合并单元格
    def handleMergedCells(self, wsSrc, wsTag):
        print(wsSrc.merged_cells.ranges)  # 获取所有合并单元格
        mergedCellsList = wsSrc.merged_cells.ranges
        maxLen = len(mergedCellsList)
        # wsTag.page_setup.orientation = wsTag.ORIENTATION_LANDSCAPE
        # wsTag.page_setup.paperSize = wsTag.PAPERSIZE_TABLOID
        # wsTag.page_setup.fitToHeight = 3
        # wsTag.page_setup.fitToWidth = 0
        if len(mergedCellsList) > 0:
            for i in range(0, maxLen):
                print("mergedCellsList length: %d" % len(mergedCellsList))
                mergeCells = mergedCellsList[0]
                tagCell = str(mergedCellsList[0])
                cellNum = tagCell.split(":")
                wsSrc.unmerge_cells(tagCell)
                cellValue = wsSrc[cellNum[0]].value
                # 设置sheet标签颜色
                # wsTag.sheet_properties.tabColor = "1072BA"
                try:
                    wsTag.merge_cells(range_string=tagCell)
                    #wsTag.cell(row=mergeCells.min_row, column=mergeCells.min_col, value=cellValue)
                    #设置单元格样式
                    thin = Side(color="000000", border_style="thin")
                    thick = Side(color="000000", border_style="thick")
                    focus_cell = wsTag[cellNum[0]]
                    focus_cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                    focus_cell.fill = PatternFill("solid", fgColor="8DB4E2")
                    focus_cell.font = Font(name="宋体", color="000000")
                    focus_cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
                except (TypeError, ValueError) as e:
                    print(e)
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    raise
                # print("tagCell : %s" % tagCell, "top cell: %s" % cellValue.value, "i : %d" % i)
    #处理单个单元格
    def handleSingleCell(self, wsSrc, wsTag):
        print(wsSrc.rows)

        for row in wsSrc.rows:
            for cell in row:
                cell_pos = cell.coordinate
                if cell.value != None:
                    wsTag[cell_pos] = cell.value
                    #设置单元格样式
                    thin = Side(color="000000", border_style="thin")
                    focus_cell = wsTag[cell_pos]
                    focus_cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)
                    focus_cell.fill = PatternFill("solid", fgColor="8DB4E2")
                    focus_cell.font = Font(name="宋体", color="000000")
                    focus_cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

        pass

'''
copy excel thread
'''
threadLock = threading.Lock()
class copyExcel(threading.Thread):

    def __init__(self, threadID, name, src_file, tag_file, sheet_name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.src_file = src_file
        self.tag_file = tag_file
        self.sheet_name = sheet_name
    def run(self):
        threadLock.acquire()
        newExcelReport = reportExcel(self.threadID)
        print("ThreadID:%d, Thread Name:%s", self.threadID, self.name)
        newExcelReport.replace_xls(self.src_file, self.tag_file, self.sheet_name)
        memberList.append(self.sheet_name)
        threadLock.release()


'''
ui handle thread, main thread
'''
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
        self.listWidget_filelist.clear()
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
       #self.summaryReportWork = openpyxl.load_workbook(summaryWorkPath)
       threadID = 0
       for reportWork in self.personReportPathList:
           curReportPath = self.directory + '/' + reportWork
           self.memberName = self.getStrBetweenSymbol(reportWork, '_', '.')
           #self.replace_xls(curReportPath, summaryWorkPath, memberName)
           generateThread = copyExcel(threadID, "Thread-"+str(threadID), curReportPath, summaryWorkPath, self.memberName )
           threadID += 1
       if len(memberList) != 0:
           self.listWidget_info.addItem(self.memberName)
           memberList.remove(self.memberName )
       self.listWidget_info.addItem("周报生成完成")

    # self.personReportWork
    # noinspection PyMethodMayBeStatic
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
