# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YTDownloader\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 162)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.urlinput = QtWidgets.QLineEdit(self.centralwidget)
        self.urlinput.setObjectName("urlinput")
        self.horizontalLayout.addWidget(self.urlinput)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.addbutton = QtWidgets.QPushButton(self.centralwidget)
        self.addbutton.setObjectName("addbutton")
        self.horizontalLayout_3.addWidget(self.addbutton)
        self.downloadbutton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadbutton.setObjectName("downloadbutton")
        self.horizontalLayout_3.addWidget(self.downloadbutton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuDatei = QtWidgets.QMenu(self.menuBar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menuBar)
        self.action_download_path = QtWidgets.QAction(MainWindow)
        self.action_download_path.setObjectName("action_download_path")
        self.menuDatei.addAction(self.action_download_path)
        self.menuBar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloader"))
        self.urlinput.setPlaceholderText(_translate("MainWindow", "YouTube Url"))
        self.checkBox.setText(_translate("MainWindow", "Video"))
        self.addbutton.setText(_translate("MainWindow", "Add"))
        self.downloadbutton.setText(_translate("MainWindow", "Download All"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.action_download_path.setText(_translate("MainWindow", "Dowload Pfad"))
