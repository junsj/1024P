# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v1.ui'
#
# Created: Thu Jan  3 16:10:27 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 411)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(21, 101, 521, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.p_pic = QtGui.QLabel(self.centralwidget)
        self.p_pic.setGeometry(QtCore.QRect(560, 100, 181, 261))
        self.p_pic.setObjectName("p_pic")
        self.pb_download = QtGui.QPushButton(self.centralwidget)
        self.pb_download.setGeometry(QtCore.QRect(560, 10, 181, 61))
        self.pb_download.setObjectName("pb_download")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 521, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label1 = QtGui.QLabel(self.layoutWidget)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.p_path = QtGui.QLineEdit(self.layoutWidget)
        self.p_path.setObjectName("p_path")
        self.gridLayout.addWidget(self.p_path, 0, 1, 1, 1)
        self.pb_find = QtGui.QPushButton(self.layoutWidget)
        self.pb_find.setObjectName("pb_find")
        self.gridLayout.addWidget(self.pb_find, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setEnabled(True)
        self.label.setLineWidth(2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.progressBar = QtGui.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.p_name = QtGui.QLabel(self.layoutWidget)
        self.p_name.setScaledContents(True)
        self.p_name.setObjectName("p_name")
        self.verticalLayout.addWidget(self.p_name)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "XP1024 #PeiHuA.2019", None, QtGui.QApplication.UnicodeUTF8))
        self.p_pic.setText(QtGui.QApplication.translate("MainWindow", "pic", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_download.setText(QtGui.QApplication.translate("MainWindow", "下载", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("MainWindow", "下载路径", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_find.setText(QtGui.QApplication.translate("MainWindow", "浏览", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "下载深度", None, QtGui.QApplication.UnicodeUTF8))
        self.p_name.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

