# -*- coding: utf-8 -*-
# @Time : 2020/8/12 19:47
# @Author : johnsonLT
# @Site : 
# @File : main.py
# @Software: PyCharm

import sys
import WeeklyReports
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore


class AgentUI(QMainWindow):

    def __init__(self):
        super(AgentUI, self).__init__()
        self.initUI()
    def initUI(self):
        self.ui = WeeklyReports.Ui_MainWindow()
        self.ui.setupUi(self)  # 向主窗口添加控件
        self.ui.btn_select.clicked.connect(self.on_lineShow)
    #注释掉装饰器,打印会执行两次
    #QtCore.pyqtSlot(str, str)可以携带参数的
    # @QtCore.pyqtSlot(object)
    # def on_btn_select_clicked(self, linePath):
    #     print("select btn pressed!")
    def on_linePathShow(self):
        self.ui.line_path.setText("E:\\python")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AgentUI()
    main.show()
    sys.exit(app.exec())
