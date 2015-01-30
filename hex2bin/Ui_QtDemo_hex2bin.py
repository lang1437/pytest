# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QtDemo\QtDemo_hex2bin.ui'
#
# Created: Fri Jan 24 16:58:20 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QtDemo_Hex2Bin(object):
    def setupUi(self, QtDemo_Hex2Bin):
        QtDemo_Hex2Bin.setObjectName(_fromUtf8("QtDemo_Hex2Bin"))
        QtDemo_Hex2Bin.resize(562, 520)
        self.centralWidget = QtGui.QWidget(QtDemo_Hex2Bin)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 521, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.openfirstfileButton = QtGui.QPushButton(self.groupBox)
        self.openfirstfileButton.setGeometry(QtCore.QRect(430, 20, 75, 23))
        self.openfirstfileButton.setObjectName(_fromUtf8("openfirstfileButton"))
        self.opensecondfileButton = QtGui.QPushButton(self.groupBox)
        self.opensecondfileButton.setGeometry(QtCore.QRect(430, 50, 75, 23))
        self.opensecondfileButton.setObjectName(_fromUtf8("opensecondfileButton"))
        self.secondlineEdit = QtGui.QLineEdit(self.groupBox)
        self.secondlineEdit.setGeometry(QtCore.QRect(100, 50, 321, 20))
        self.secondlineEdit.setObjectName(_fromUtf8("secondlineEdit"))
        self.firstlineEdit = QtGui.QLineEdit(self.groupBox)
        self.firstlineEdit.setGeometry(QtCore.QRect(100, 20, 321, 20))
        self.firstlineEdit.setObjectName(_fromUtf8("firstlineEdit"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 100, 521, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.mergeButton = QtGui.QPushButton(self.groupBox_2)
        self.mergeButton.setEnabled(True)
        self.mergeButton.setGeometry(QtCore.QRect(160, 20, 201, 23))
        self.mergeButton.setObjectName(_fromUtf8("mergeButton"))
        self.exitButton = QtGui.QPushButton(self.groupBox_2)
        self.exitButton.setGeometry(QtCore.QRect(430, 20, 75, 23))
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 160, 521, 341))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.statustextBrowser = QtGui.QTextBrowser(self.groupBox_3)
        self.statustextBrowser.setGeometry(QtCore.QRect(20, 20, 481, 301))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statustextBrowser.sizePolicy().hasHeightForWidth())
        self.statustextBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(9)
        self.statustextBrowser.setFont(font)
        self.statustextBrowser.setMouseTracking(False)
        self.statustextBrowser.setObjectName(_fromUtf8("statustextBrowser"))
        QtDemo_Hex2Bin.setCentralWidget(self.centralWidget)

        self.retranslateUi(QtDemo_Hex2Bin)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), QtDemo_Hex2Bin.close)
        QtCore.QMetaObject.connectSlotsByName(QtDemo_Hex2Bin)

    def retranslateUi(self, QtDemo_Hex2Bin):
        QtDemo_Hex2Bin.setWindowTitle(_translate("QtDemo_Hex2Bin", "MainWindow", None))
        self.groupBox.setTitle(_translate("QtDemo_Hex2Bin", "文件", None))
        self.openfirstfileButton.setText(_translate("QtDemo_Hex2Bin", "打开", None))
        self.opensecondfileButton.setText(_translate("QtDemo_Hex2Bin", "打开", None))
        self.label.setText(_translate("QtDemo_Hex2Bin", "第一个hex文件", None))
        self.label_2.setText(_translate("QtDemo_Hex2Bin", "第二个hex文件", None))
        self.groupBox_2.setTitle(_translate("QtDemo_Hex2Bin", "功能", None))
        self.mergeButton.setText(_translate("QtDemo_Hex2Bin", "转换并合并", None))
        self.exitButton.setText(_translate("QtDemo_Hex2Bin", "退出", None))
        self.groupBox_3.setTitle(_translate("QtDemo_Hex2Bin", "状态", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QtDemo_Hex2Bin = QtGui.QMainWindow()
    ui = Ui_QtDemo_Hex2Bin()
    ui.setupUi(QtDemo_Hex2Bin)
    QtDemo_Hex2Bin.show()
    sys.exit(app.exec_())

