# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fileOpen = QtWidgets.QPushButton(self.centralwidget)
        self.fileOpen.setEnabled(True)
        self.fileOpen.setGeometry(QtCore.QRect(370, 620, 75, 23))
        self.fileOpen.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.fileOpen.setCheckable(False)
        self.fileOpen.setChecked(False)
        self.fileOpen.setObjectName("fileOpen")
        self.fileOpen.clicked.connect(self.btnOpen)
        self.mainText = QtWidgets.QTextEdit(self.centralwidget)
        self.mainText.setGeometry(QtCore.QRect(20, 10, 561, 601))
        self.mainText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.mainText.setInputMethodHints(QtCore.Qt.ImhNone)
        self.mainText.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.mainText.setObjectName("mainText")
        self.fileSave = QtWidgets.QPushButton(self.centralwidget)
        self.fileSave.setGeometry(QtCore.QRect(370, 650, 75, 23))
        self.fileSave.setObjectName("fileSave")
        self.fileSave.clicked.connect(self.btnSave)
        self.openPath = QtWidgets.QLineEdit(self.centralwidget)
        self.openPath.setGeometry(QtCore.QRect(20, 620, 331, 20))
        self.openPath.setObjectName("openPath")
        self.saveName = QtWidgets.QLineEdit(self.centralwidget)
        self.saveName.setGeometry(QtCore.QRect(20, 650, 331, 20))
        self.saveName.setObjectName("saveName")
        self.ANSI = QtWidgets.QRadioButton(self.centralwidget)
        self.ANSI.setGeometry(QtCore.QRect(460, 630, 90, 16))
        self.ANSI.setObjectName("ANSI")
        self.UTF = QtWidgets.QRadioButton(self.centralwidget)
        self.UTF.setGeometry(QtCore.QRect(460, 650, 90, 16))
        self.UTF.setObjectName("UTF")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fileOpen.setText(_translate("MainWindow", "Open"))
        self.fileOpen.setShortcut(_translate("MainWindow", "Return"))
        self.fileSave.setText(_translate("MainWindow", "Save"))
        self.fileSave.setShortcut(_translate("MainWindow", "Return"))
        self.ANSI.setText(_translate("MainWindow", "ANSI"))
        self.UTF.setText(_translate("MainWindow", "UTF-8"))

    
    
    def btnOpen(self) :
        s = self.openPath.text()
        if self.ANSI.isChecked() :
            f = open(s, 'r', encoding = 'ANSI')
            self.mainText.setText(f.read())
        elif self.UTF.isChecked() :
            f = open(s, 'r', encoding = 'UTF-8')
            self.mainText.setText(f.read())
        

    def btnSave(self) :
        s = self.mainText.toPlainText()
        s_path = self.saveName.text()
        if self.UTF.isChecked() :
            f = open(s_path, 'w', encoding = 'utf-8')
            f.write(s)
        elif self.ANSI.isChecked() :
            f = open(s_path, 'w', encoding = 'ANSI')
            f.write(s)
           

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
