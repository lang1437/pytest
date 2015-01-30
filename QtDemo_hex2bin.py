# -*- coding: utf-8 -*-

"""
Module implementing QtDemoHex2binMerge.
"""
import sys,os

from PyQt4 import  QtGui, QtCore
import intelhex

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QMainWindow

from Ui_QtDemo_hex2bin import Ui_QtDemo_Hex2Bin

#print("loop")
class QtDemoHex2binMerge(QMainWindow, Ui_QtDemo_Hex2Bin):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Hex2Bin --- by QuetuiLang")
        self.setFixedSize(562, 520)
        
        #self.connect(openfirstfileButton,SIGNAL("clicked()"),self.openFile) 
        #print('mainloop')
        exitApp = QtGui.QAction(QtGui.QIcon('icon/pyc.ico'), '退出', self)
        exitApp.setShortcut('Ctrl+Q')
        exitApp.setStatusTip('Exit application')
        self.connect(exitApp, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        #helpApp = QtGui.QAction(QtGui.QIcon('icon/pyc.ico'),'说明', self)
        helpApp = QtGui.QAction(self)
        helpApp.setText('软件说明')
        helpApp.setShortcut('F1')
        helpApp.setStatusTip('Help application')
        self.connect(helpApp, QtCore.SIGNAL('triggered()'), self.createHelpDialog)
        
        verApp = QtGui.QAction(self)
        verApp.setText('版本')
        verApp.setStatusTip('Version application')
        self.connect(verApp, QtCore.SIGNAL('triggered()'), self.createVerDialog)
        #helpApp = QtGui.QAction(QtGui.QFileDialog("CS"), self)
        #self.connect(helpApp, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        self.statusBar() 
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('菜单')
        fileMenu.addAction(exitApp)
        
        helpMenu = menubar.addMenu('帮助')
        helpMenu.addAction(helpApp)
        helpMenu.addAction(verApp)
        
    #@pyqtSlot()
    def createHelpDialog(self):
        # TODO: not implemented yet
        self.statustextBrowser.setText("软件实现的是将两个Hex文件同时转为Bin文件并且合并为一个Bin文件输出的功能。") 
        self.statustextBrowser.append("专用于二次boot程序与加密磁头程序的转换并合并。")
        #raise NotImplementedError
        
    @pyqtSlot()
    def createVerDialog(self):
        # TODO: not implemented yet
        self.statustextBrowser.setText("Hex2bin Version 0.0.1") 
        #raise NotImplementedError
    
    @pyqtSlot()
    def on_mergeButton_clicked(self):
        #error
        tmpFirstHex = self.firstlineEdit.text()
        tmpSecondHex = self.secondlineEdit.text()
        if(tmpFirstHex == '' or tmpSecondHex == ''):
            #print('error')
            errInput = QtGui.QMessageBox.warning(self, '提示',"请选择两个hex文件，注意顺序", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            if errInput == QtGui.QMessageBox.Yes:
                return
            
            #自定义对话框
            #customMsgBox=QtGui.QMessageBox(self)  
            #customMsgBox.setWindowTitle("提示")  
            #customMsgBox.addButton("确定", QtGui.QMessageBox.ActionRole)  
            #customMsgBox.addButton(self.tr("解锁"), QtGui.QMessageBox.ActionRole)  
            #customMsgBox.addButton("cancel",QtGui.QMessageBox.ActionRole)  
      
            #customMsgBox.setText("请选择两个hex文件，注意顺序!")  
            #customMsgBox.exec_() 
        else:
            #firstHex = os.path.basename(self.firstlineEdit.text())
            #secondHex = os.path.basename(self.secondlineEdit.text())
            curFirstPath = os.path.abspath(self.firstlineEdit.text())
            curSecondPath = os.path.abspath(self.secondlineEdit.text())
            
            #get file name
            #tmp_name = os.path.basename(firstHex)
            binfile1 = curFirstPath[0:-4] + '.bin'
            #tmp_name = os.path.basename(secondHex)
            binfile2 = curSecondPath[0:-4] + '~' + '.bin'
            
            binfile_name = curSecondPath[0:-4] + '.bin'
            if(os.path.isfile(binfile_name)):
                os.remove(binfile_name)
            
            #hex to bin
            self.statustextBrowser.setText("Hex to Bin and Merge Bin file....") 
            self.statustextBrowser.append("Hex File To Bin File...")
            self.statustextBrowser.append("*****************************")
            #self.statustextBrowser.append(firstHex)
            #self.statustextBrowser.append(secondHex)
            self.statustextBrowser.append(curFirstPath)
            self.statustextBrowser.append(curSecondPath)
            self.statustextBrowser.append(binfile1)
            self.statustextBrowser.append(binfile2)
            
            self.statustextBrowser.append("*****************************")
            #self.statustextBrowser.append("")
            
            intelhex.hex2bin(curFirstPath, binfile1, None, None, None, 00)
            intelhex.hex2bin(curSecondPath, binfile2, None, None, None, 00)
            
            self.statustextBrowser.append("Hex File To Bin File completly")
            
            #merge two files
            self.statustextBrowser.append(binfile1)
            self.statustextBrowser.append(binfile2)
            
            bin_boot_len = os.path.getsize(binfile1)
            bin_app_len = os.path.getsize(binfile2)
            self.statustextBrowser.append("First Bin File size is %d" %(bin_boot_len))
            self.statustextBrowser.append("Second Bin File size is %d" %(bin_app_len))
            
            bin_boot_file = open(binfile1, 'rb')
            bin_app_file = open(binfile2, 'rb')
            bin_file = open(binfile_name, 'ab')
            
            for h in bin_boot_file.readlines():
                #print(h)
                bin_file.write(h)
                
            bin_file.seek(2)
            bin_app_file.seek(bin_boot_len, 0)
            for h in bin_app_file.readlines():
                #print(h)
                bin_file.write(h)
                
            bin_boot_file.close()
            bin_app_file.close()
            bin_file.close()
            
            bin_file_len = os.path.getsize(binfile_name)
            self.statustextBrowser.append("Bin File size is %d "%bin_file_len)
            self.statustextBrowser.append("")
        # TODO: not implemented yet
        #raise NotImplementedError
        
    
    @pyqtSlot()
    def on_openfirstfileButton_clicked(self):
        """
        Slot documentation goes here.  
        """
        # TODO: not implemented yet
        hexfile1 = QtGui.QFileDialog.getOpenFileName(self,"Open First hexfile","","hex files(*.hex)")
        self.firstlineEdit.setText(str(hexfile1)) 
        self.firstlineEdit.text()
        #raise NotImplementedError
    
    @pyqtSlot()
    def on_opensecondfileButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        hexfile2 = QtGui.QFileDialog.getOpenFileName(self,"Open Second hexfile","","hex files(*.hex)")
        self.secondlineEdit.setText(str(hexfile2))
        #raise NotImplementedError

if __name__ == "__main__":
    app_merge = QtGui.QApplication(sys.argv)
    button_merge = QtDemoHex2binMerge()
    button_merge.show()
    sys.exit(app_merge.exec_())
