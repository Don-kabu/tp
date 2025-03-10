# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views\ui\error.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from .icons import img_rc




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 300)
        Dialog.setMinimumSize(QtCore.QSize(700, 300))
        Dialog.setMaximumSize(QtCore.QSize(700, 300))
        Dialog.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(240, 200, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_ok.setFont(font)
        self.btn_ok.setStyleSheet("background:rgb(116,116,116);\n"
"color: white;\n"
"border-radius: 20px;\n"
"padding: 5px;")
        self.btn_ok.setObjectName("btn_ok")
        self.info = QtWidgets.QLabel(Dialog)
        self.info.setGeometry(QtCore.QRect(170, 40, 491, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.info.setFont(font)
        self.info.setStyleSheet("color: red;")
        self.info.setObjectName("info")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":ok/icons/circle-exclamation.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_ok.setText(_translate("Dialog", "ok"))
        self.info.setText(_translate("Dialog", "connection avec succes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
