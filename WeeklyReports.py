# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeeklyReports.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_path = QtWidgets.QLineEdit(self.centralwidget)
        self.line_path.setObjectName("line_path")
        self.horizontalLayout_2.addWidget(self.line_path)
        self.btn_select = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select.setObjectName("btn_select")
        self.horizontalLayout_2.addWidget(self.btn_select)
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setObjectName("btn_generate")
        self.horizontalLayout_2.addWidget(self.btn_generate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listWidget_filelist = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_filelist.setObjectName("listWidget_filelist")
        self.horizontalLayout_3.addWidget(self.listWidget_filelist)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setMaximumSize(QtCore.QSize(388, 16777215))
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.listWidget_info = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_info.setObjectName("listWidget_info")
        self.verticalLayout.addWidget(self.listWidget_info)
        self.verticalLayout.setStretch(0, 2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.btn_select.clicked.connect(self.line_path.show)
        self.btn_generate.clicked.connect(self.listWidget_filelist.showNormal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "周报管理"))
        self.btn_select.setText(_translate("MainWindow", "选择"))
        self.btn_generate.setText(_translate("MainWindow", "生成"))

