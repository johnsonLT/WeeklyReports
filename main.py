# -*- coding: utf-8 -*-
# @Time : 2020/8/12 19:47
# @Author : johnsonLT
# @Site : 
# @File : main.py
# @Software: PyCharm

import sys
import WeeklyReports
from PyQt5.QtWidgets import QApplication, QMainWindow


class AgentUI(QMainWindow):
    def __init__(self):
        super(AgentUI, self).__init__()
        self.initUI()

    def initUI(self):
        ui = WeeklyReports.Ui_MainWindow()
        ui.setupUi(self)  # 向主窗口添加控件


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AgentUI()
    main.show()
    sys.exit(app.exec())
