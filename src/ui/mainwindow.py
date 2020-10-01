# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(260, 400)
        MainWindow.setMaximumSize(QSize(320, 480))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.programLoaderButton = QPushButton(MainWindow)
        self.programLoaderButton.setObjectName(u"programLoaderButton")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.programLoaderButton.sizePolicy().hasHeightForWidth())
        self.programLoaderButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.programLoaderButton)

        self.remoteControlButton = QPushButton(MainWindow)
        self.remoteControlButton.setObjectName(u"remoteControlButton")
        sizePolicy.setHeightForWidth(self.remoteControlButton.sizePolicy().hasHeightForWidth())
        self.remoteControlButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.remoteControlButton)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.programLoaderButton.setText(QCoreApplication.translate("MainWindow", u"Program Loader", None))
        self.remoteControlButton.setText(QCoreApplication.translate("MainWindow", u"Remote Control", None))
    # retranslateUi

