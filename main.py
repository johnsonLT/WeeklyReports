# -*- coding: utf-8 -*-
# @Time : 2020/8/12 19:47
# @Author : johnsonLT
# @Site : 
# @File : main.py
# @Software: PyCharm

import sys
import WeeklyReports
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)  #应用程序
    mainWindow = QMainWindow()  #主窗口
    ui = WeeklyReports.Ui_MainWindow()
    ui.setupUi(mainWindow)  #向主窗口添加控件
    mainWindow.show()
    sys.exit(app.exec())