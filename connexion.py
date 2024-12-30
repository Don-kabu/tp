# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/connexion.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 825)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/D:/Minimalistic-Flat-Modern-GUI-Template-master/Minimalistic-Flat-Modern-GUI-Template-master/images/Layout/frontpageAsset 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(110, 90, 861, 591))
        self.widget.setObjectName("widget")
        self.leftpanel = QtWidgets.QFrame(self.widget)
        self.leftpanel.setGeometry(QtCore.QRect(0, 0, 441, 591))
        self.leftpanel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-image: url(:/icons/python/icons/backgroun lo0gin.jpg); \n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;")
        self.leftpanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftpanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftpanel.setObjectName("leftpanel")
        self.loginbutton = QtWidgets.QPushButton(self.leftpanel)
        self.loginbutton.setGeometry(QtCore.QRect(100, 500, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet("background:rgb(116,116,116);\n"
"color: white;\n"
"border-radius: 20px;\n"
"padding: 5px;")
        self.loginbutton.setObjectName("loginbutton")
        self.label_5 = QtWidgets.QLabel(self.leftpanel)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: transparent ;\n"
"color: blue;")
        self.label_5.setObjectName("label_5")
        self.leftpanel_2 = QtWidgets.QFrame(self.widget)
        self.leftpanel_2.setGeometry(QtCore.QRect(440, 0, 421, 591))
        self.leftpanel_2.setStyleSheet("background-color: rgb(52, 52, 52);\n"
"color: rgb(116,116,116);")
        self.leftpanel_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftpanel_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftpanel_2.setObjectName("leftpanel_2")
        self.label = QtWidgets.QLabel(self.leftpanel_2)
        self.label.setGeometry(QtCore.QRect(0, 20, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setStyleSheet("color:rgb(116, 116, 116);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(5)
        self.label.setMidLineWidth(5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.leftpanel_2)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.leftpanel_2)
        self.label_3.setGeometry(QtCore.QRect(30, 370, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(self.leftpanel_2)
        self.username.setGeometry(QtCore.QRect(20, 220, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setStyleSheet("border:none;\n"
"border-bottom: 4px solid rgb(115, 115, 115) ;")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.leftpanel_2)
        self.password.setGeometry(QtCore.QRect(30, 400, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setStyleSheet("border:none;\n"
"border-bottom: 4px solid rgb(115, 115, 115) ;\n"
"")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.bt_login = QtWidgets.QPushButton(self.leftpanel_2)
        self.bt_login.setGeometry(QtCore.QRect(90, 500, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bt_login.setFont(font)
        self.bt_login.setStyleSheet("\n"
"QPushButton {\n"
"    background:none;\n"
"    border: none;\n"
"    background-color: rgb(65, 157, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(140, 140, 140);\n"
"    \n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"")
        self.bt_login.setObjectName("bt_login")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 21))
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
        self.loginbutton.setText(_translate("MainWindow", "signin"))
        self.label_5.setText(_translate("MainWindow", "connect to get vacation"))
        self.label.setText(_translate("MainWindow", "connexion"))
        self.label_2.setText(_translate("MainWindow", "username"))
        self.label_3.setText(_translate("MainWindow", "password"))
        self.bt_login.setText(_translate("MainWindow", "login"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())