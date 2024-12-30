# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/newtypevac.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1352, 802)
        MainWindow.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_bottom_west = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom_west.setGeometry(QtCore.QRect(0, -20, 120, 771))
        self.frame_bottom_west.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_bottom_west.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet("background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_bottom_west.setObjectName("frame_bottom_west")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_home = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_home.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_home.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_home.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_home.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_home.setObjectName("frame_home")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.bn_home = QtWidgets.QPushButton(self.frame_home)
        self.bn_home.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_home.setMaximumSize(QtCore.QSize(160, 55))
        self.bn_home.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/python/icons/house.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_home.setIcon(icon)
        self.bn_home.setIconSize(QtCore.QSize(50, 50))
        self.bn_home.setFlat(True)
        self.bn_home.setObjectName("bn_home")
        self.horizontalLayout_15.addWidget(self.bn_home)
        self.verticalLayout_3.addWidget(self.frame_home)
        self.frame_bug = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_bug.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_bug.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_bug.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bug.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_bug.setObjectName("frame_bug")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_bug)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.btn_about = QtWidgets.QPushButton(self.frame_bug)
        self.btn_about.setMinimumSize(QtCore.QSize(80, 55))
        self.btn_about.setMaximumSize(QtCore.QSize(160, 55))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_about.setFont(font)
        self.btn_about.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/python/icons/users-gear.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_about.setIcon(icon1)
        self.btn_about.setIconSize(QtCore.QSize(50, 50))
        self.btn_about.setFlat(True)
        self.btn_about.setObjectName("btn_about")
        self.horizontalLayout_16.addWidget(self.btn_about)
        self.verticalLayout_3.addWidget(self.frame_bug)
        self.frame_cloud = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_cloud.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_cloud.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_cloud.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_cloud.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_cloud.setObjectName("frame_cloud")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_cloud)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.bt_new = QtWidgets.QPushButton(self.frame_cloud)
        self.bt_new.setMinimumSize(QtCore.QSize(80, 55))
        self.bt_new.setMaximumSize(QtCore.QSize(160, 55))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_new.setFont(font)
        self.bt_new.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(0,143,150);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(0,143,150);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/python/icons/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_new.setIcon(icon2)
        self.bt_new.setIconSize(QtCore.QSize(50, 50))
        self.bt_new.setFlat(True)
        self.bt_new.setObjectName("bt_new")
        self.horizontalLayout_17.addWidget(self.bt_new)
        self.verticalLayout_3.addWidget(self.frame_cloud)
        self.frame_android = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_android.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_android.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_android.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_android.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_android.setObjectName("frame_android")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_android)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.btn_dashboard = QtWidgets.QPushButton(self.frame_android)
        self.btn_dashboard.setMinimumSize(QtCore.QSize(80, 55))
        self.btn_dashboard.setMaximumSize(QtCore.QSize(160, 55))
        self.btn_dashboard.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/python/icons/tachograph-digital.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dashboard.setIcon(icon3)
        self.btn_dashboard.setIconSize(QtCore.QSize(50, 50))
        self.btn_dashboard.setFlat(True)
        self.btn_dashboard.setObjectName("btn_dashboard")
        self.horizontalLayout_18.addWidget(self.btn_dashboard)
        self.verticalLayout_3.addWidget(self.frame_android)
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setGeometry(QtCore.QRect(80, -10, 1253, 80))
        self.frame_top.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_top_east = QtWidgets.QFrame(self.frame_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.frame_top_east.sizePolicy().hasHeightForWidth())
        self.frame_top_east.setSizePolicy(sizePolicy)
        self.frame_top_east.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_top_east.setMaximumSize(QtCore.QSize(1677721, 100))
        self.frame_top_east.setStyleSheet("background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top_east.setObjectName("frame_top_east")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_appname = QtWidgets.QFrame(self.frame_top_east)
        self.frame_appname.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_appname.setObjectName("frame_appname")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.username = QtWidgets.QLabel(self.frame_appname)
        self.username.setEnabled(True)
        self.username.setMinimumSize(QtCore.QSize(300, 50))
        self.username.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.username.setFont(font)
        self.username.setStyleSheet("color:rgb(255,255,255);")
        self.username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.username.setObjectName("username")
        self.horizontalLayout_10.addWidget(self.username)
        self.usertype = QtWidgets.QLabel(self.frame_appname)
        self.usertype.setEnabled(True)
        self.usertype.setMinimumSize(QtCore.QSize(300, 50))
        self.usertype.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.usertype.setFont(font)
        self.usertype.setStyleSheet("color:rgb(255,255,255);")
        self.usertype.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.usertype.setObjectName("usertype")
        self.horizontalLayout_10.addWidget(self.usertype)
        self.horizontalLayout_4.addWidget(self.frame_appname)
        self.frame_close = QtWidgets.QFrame(self.frame_top_east)
        self.frame_close.setMinimumSize(QtCore.QSize(55, 55))
        self.frame_close.setMaximumSize(QtCore.QSize(55, 55))
        self.frame_close.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_close.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_close.setObjectName("frame_close")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bn_close = QtWidgets.QPushButton(self.frame_close)
        self.bn_close.setMaximumSize(QtCore.QSize(55, 55))
        self.bn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color:rgb(255, 8, 45) ;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_close.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/python/icons/xmark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_close.setIcon(icon4)
        self.bn_close.setIconSize(QtCore.QSize(50, 50))
        self.bn_close.setFlat(True)
        self.bn_close.setObjectName("bn_close")
        self.horizontalLayout_5.addWidget(self.bn_close)
        self.horizontalLayout_4.addWidget(self.frame_close)
        self.horizontalLayout.addWidget(self.frame_top_east)
        self.user_infoframe = QtWidgets.QFrame(self.centralwidget)
        self.user_infoframe.setGeometry(QtCore.QRect(120, 70, 1231, 671))
        self.user_infoframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_infoframe.setFrameShadow(QtWidgets.QFrame.Plain)
        self.user_infoframe.setObjectName("user_infoframe")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.user_infoframe)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.user_infoframe)
        font = QtGui.QFont()
        font.setPointSize(64)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.user_infoframe)
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 500))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 500))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255,255,255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255,255,255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.delete_2 = QtWidgets.QPushButton(self.frame_2)
        self.delete_2.setEnabled(True)
        self.delete_2.setMinimumSize(QtCore.QSize(100, 50))
        self.delete_2.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.delete_2.setFont(font)
        self.delete_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(51,51,51);\n"
"    border-radius: 5px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {    \n"
"    background-color: rgb(112,112,112);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/python/icons/trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_2.setIcon(icon5)
        self.delete_2.setIconSize(QtCore.QSize(30, 30))
        self.delete_2.setObjectName("delete_2")
        self.gridLayout_2.addWidget(self.delete_2, 4, 1, 1, 1)
        self.postnom = QtWidgets.QLineEdit(self.frame_2)
        self.postnom.setMinimumSize(QtCore.QSize(400, 25))
        self.postnom.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.postnom.setFont(font)
        self.postnom.setStyleSheet("QLineEdit {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(51,51,51);\n"
"    border-radius:4px;\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(112,112,112);\n"
"    border-radius:4px;\n"
"    background:rgb(112,112,112);\n"
"}")
        self.postnom.setObjectName("postnom")
        self.gridLayout_2.addWidget(self.postnom, 1, 1, 1, 2)
        self.nom = QtWidgets.QLineEdit(self.frame_2)
        self.nom.setEnabled(True)
        self.nom.setMinimumSize(QtCore.QSize(400, 25))
        self.nom.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.nom.setFont(font)
        self.nom.setStyleSheet("QLineEdit {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(51,51,51);\n"
"    border-radius:4px;\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(112,112,112);\n"
"    border-radius:4px;\n"
"    background:rgb(112,112,112);\n"
"}")
        self.nom.setObjectName("nom")
        self.gridLayout_2.addWidget(self.nom, 0, 1, 1, 2)
        self.addemployer = QtWidgets.QPushButton(self.frame_2)
        self.addemployer.setMinimumSize(QtCore.QSize(100, 50))
        self.addemployer.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.addemployer.setFont(font)
        self.addemployer.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(51,51,51);\n"
"    border-radius: 5px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {    \n"
"    border-radius: 5px;    \n"
"    border: 2px solid rgb(112,112,112);\n"
"    background-color: rgb(112,112,112);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/python/icons/check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addemployer.setIcon(icon6)
        self.addemployer.setIconSize(QtCore.QSize(30, 30))
        self.addemployer.setObjectName("addemployer")
        self.gridLayout_2.addWidget(self.addemployer, 4, 2, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1352, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.img = QtWidgets.QAction(MainWindow)
        self.img.setObjectName("img")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bn_home.setToolTip(_translate("MainWindow", "Home"))
        self.bn_home.setText(_translate("MainWindow", "home"))
        self.btn_about.setToolTip(_translate("MainWindow", "Bug"))
        self.btn_about.setText(_translate("MainWindow", "see"))
        self.bt_new.setToolTip(_translate("MainWindow", "Cloud"))
        self.bt_new.setText(_translate("MainWindow", "new"))
        self.btn_dashboard.setToolTip(_translate("MainWindow", "Android"))
        self.btn_dashboard.setText(_translate("MainWindow", "dashboard"))
        self.username.setText(_translate("MainWindow", "<html><head/><body><p>admin</p><p><br/></p></body></html>"))
        self.usertype.setText(_translate("MainWindow", "<html><head/><body><p>precieux</p><p><br/></p></body></html>"))
        self.bn_close.setToolTip(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", "new type of vacation"))
        self.label_2.setText(_translate("MainWindow", "nom :"))
        self.label_3.setText(_translate("MainWindow", "libeele"))
        self.delete_2.setText(_translate("MainWindow", "Clear"))
        self.addemployer.setText(_translate("MainWindow", "add"))
        self.img.setText(_translate("MainWindow", "img"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())