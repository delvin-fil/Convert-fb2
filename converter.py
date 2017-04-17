# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converter.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(656, 354)
        self.textIn = QtWidgets.QTextEdit(Form)
        self.textIn.setGeometry(QtCore.QRect(10, 10, 521, 131))
        self.textIn.setObjectName("textIn")
        self.btnQuit = QtWidgets.QPushButton(Form)
        self.btnQuit.setGeometry(QtCore.QRect(540, 70, 105, 25))
        self.btnQuit.setDefault(True)
        self.btnQuit.setObjectName("btnQuit")
        self.showd = QtWidgets.QPushButton(Form)
        self.showd.setGeometry(QtCore.QRect(540, 10, 105, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showd.sizePolicy().hasHeightForWidth())
        self.showd.setSizePolicy(sizePolicy)
        self.showd.setSizeIncrement(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.showd.setPalette(palette)
        self.showd.setDefault(True)
        self.showd.setFlat(False)
        self.showd.setObjectName("showd")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 290, 631, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mylabel = QtWidgets.QLabel(self.layoutWidget)
        self.mylabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mylabel.setObjectName("mylabel")
        self.horizontalLayout.addWidget(self.mylabel)
        self.textOut = QtWidgets.QTextEdit(Form)
        self.textOut.setGeometry(QtCore.QRect(10, 150, 521, 131))
        self.textOut.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textOut.setObjectName("textOut")
        self.btnConv = QtWidgets.QPushButton(Form)
        self.btnConv.setGeometry(QtCore.QRect(540, 40, 105, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 237, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnConv.setPalette(palette)
        self.btnConv.setDefault(True)
        self.btnConv.setObjectName("btnConv")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 320, 631, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.layoutWidget.raise_()
        self.textIn.raise_()
        self.btnQuit.raise_()
        self.showd.raise_()
        self.textOut.raise_()
        self.btnConv.raise_()
        self.progressBar.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "fb2 to txt converter"))
        self.btnQuit.setText(_translate("Form", "Exit"))
        self.showd.setText(_translate("Form", " Open File"))
        self.mylabel.setText(_translate("Form", "Empty"))
        self.btnConv.setText(_translate("Form", "Save convert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

