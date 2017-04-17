#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import re
import sys
import warnings
import lxml.etree as et
from PyQt5 import (QtCore, QtGui, uic, QtWidgets)
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog,
                             QApplication, QProgressBar)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

warnings.filterwarnings("ignore")
Form, Base = uic.loadUiType("converter.ui")




class MyWindow(QtWidgets.QWidget, Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Form()
        self.ui.setupUi(self)
        self.timer = QBasicTimer()
        self.step = 0
        self.ui.btnQuit.clicked.connect(QCoreApplication.instance().quit)
        self.ui.showd.clicked.connect(self.getfiles)
        self.ui.btnConv.clicked.connect(self.convertfiles)
        self.setGeometry(300, 400, 656, 354)

    def getfiles(self):

        fname = QFileDialog.getOpenFileName(self, "Open fb2", "/home/", "FictionBook Files (*.fb2)")[0]

        with open(fname, 'r') as data:
            data = data.read()
            self.ui.textIn.setText(data)
            self.ui.mylabel.setText(f'Input file: {fname}')

        global fout
        fout = re.sub(r'\.fb2', '', fname)
        fout = fout + '.txt'

        with open(fname, 'rb') as f_in, open(fout, 'w') as f_out:
            check = f_in.read()

            #check = bytes(bytearray(f_in.read(), encoding='utf-8'))
            tree = et.fromstring(check)
            ns = {'ns': "http://www.gribuser.ru/xml/fictionbook/2.0"}
            for bin_eb in tree.xpath('//ns:binary', namespaces=ns):
                bin_eb.getparent().remove(bin_eb)
            for bin_ed in tree.xpath('//ns:description', namespaces=ns):
                bin_ed.getparent().remove(bin_ed)
            global cleart, cleart2
            cleart = et.tounicode(tree)
            cleart = re.sub(r'\<[^>]*\>', '', cleart)
            self.ui.textOut.setText(cleart)

    def convertfiles(self):
        cleart2 = self.ui.textOut.toPlainText()
        self.ui.mylabel.setText('')
        with open(fout, 'w') as f_out:
            f_out.write(cleart2)
        self.ui.mylabel.setText(f'Saved file: {fout}')
        print(fout)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()  # Создаем экземпляр класса
    window.setWindowTitle("Ковертер Fb2 > Txt")
    window.setWindowIcon(
        QtGui.QIcon('skull.png'))  # рисуем иконку
    window.show()  # Отображаем окно

    sys.exit(app.exec_())  # Запускаем цикл обработки событий
