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
        MainWindow.resize(601, 725)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fileOpen = QtWidgets.QPushButton(self.centralwidget)
        self.fileOpen.setEnabled(True)
        self.fileOpen.setGeometry(QtCore.QRect(370, 620, 75, 23))
        self.fileOpen.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.fileOpen.setCheckable(False)
        self.fileOpen.setChecked(False)
        self.fileOpen.setObjectName("fileOpen")
        self.mainText = QtWidgets.QTextEdit(self.centralwidget)
        self.mainText.setGeometry(QtCore.QRect(20, 10, 561, 601))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.mainText.setPalette(palette)
        self.mainText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.mainText.setInputMethodHints(QtCore.Qt.ImhNone)
        self.mainText.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.mainText.setObjectName("mainText")
        self.fileSave = QtWidgets.QPushButton(self.centralwidget)
        self.fileSave.setGeometry(QtCore.QRect(370, 650, 75, 23))
        self.fileSave.setObjectName("fileSave")
        self.openPath = QtWidgets.QLineEdit(self.centralwidget)
        self.openPath.setGeometry(QtCore.QRect(20, 620, 331, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.openPath.setPalette(palette)
        self.openPath.setText("")
        self.openPath.setObjectName("openPath")
        self.saveName = QtWidgets.QLineEdit(self.centralwidget)
        self.saveName.setGeometry(QtCore.QRect(20, 650, 331, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.saveName.setPalette(palette)
        self.saveName.setObjectName("saveName")
        self.ANSI = QtWidgets.QRadioButton(self.centralwidget)
        self.ANSI.setGeometry(QtCore.QRect(460, 623, 90, 16))
        self.ANSI.setObjectName("ANSI")
        self.UTF = QtWidgets.QRadioButton(self.centralwidget)
        self.UTF.setGeometry(QtCore.QRect(460, 653, 90, 16))
        self.UTF.setObjectName("UTF")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEncoding_Option = QtWidgets.QMenu(self.menuFile)
        self.menuEncoding_Option.setObjectName("menuEncoding_Option")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuOpen = QtWidgets.QAction(MainWindow)
        self.menuOpen.setCheckable(False)
        self.menuOpen.setChecked(False)
        self.menuOpen.setObjectName("menuOpen")
        self.menuSave = QtWidgets.QAction(MainWindow)
        self.menuSave.setObjectName("menuSave")
        self.ckUTF = QtWidgets.QAction(MainWindow)
        self.ckUTF.setCheckable(True)
        self.ckUTF.setChecked(True)
        self.ckUTF.setObjectName("ckUTF")
        self.ckANSI = QtWidgets.QAction(MainWindow)
        self.ckANSI.setCheckable(True)
        self.ckANSI.setObjectName("ckANSI")
        self.menuEncoding_Option.addAction(self.ckUTF)
        self.menuEncoding_Option.addAction(self.ckANSI)
        self.menuFile.addAction(self.menuOpen)
        self.menuFile.addAction(self.menuSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuEncoding_Option.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

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
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEncoding_Option.setTitle(_translate("MainWindow", "Encoding Option"))
        self.menuOpen.setText(_translate("MainWindow", "Open"))
        self.menuOpen.setToolTip(_translate("MainWindow", "File Open Menu", "File Open"))
        self.menuOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.menuSave.setText(_translate("MainWindow", "Save"))
        self.menuSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.ckUTF.setText(_translate("MainWindow", "UTF-8"))
        self.ckANSI.setText(_translate("MainWindow", "ANSI"))
        self.menuOpen.triggered.connect(self.btn_Open)
        self.ckUTF.triggered.connect(self.check_UTF)
        self.ckANSI.triggered.connect(self.check_ANSI)
        self.menuSave.triggered.connect(self.btn_Save)

    def check_UTF(self) :
        self.ckANSI.setChecked(False)

    def check_ANSI(self) :
        self.ckUTF.setChecked(False)
        # if self.ckUTF.setChecked() == True :
        #     self.ckANSI.setChecked(False)
        # elif self.ckANSI.setChecked() == True :
        #     self.ckUTF.setChecked(False)

    def btn_Open(self) :
        a = QtWidgets.QFileDialog.getOpenFileName() 

        if self.ckUTF.isChecked() :
            enco = 'UTF-8'
        else :
            enco = 'ANSI'
        f = open(a[0], 'r', encoding = enco)
        self.mainText.setText(f.read())

    def btn_Save(self) :
        s = self.mainText.toPlainText()
        a = QtWidgets.QFileDialog.getSaveFileName() 

        if self.ckUTF.isChecked() :
            enco = 'UTF-8'
        else :
            enco = 'ANSI'
        f = open(a[0], 'w', encoding = enco)
        f.write(s)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
