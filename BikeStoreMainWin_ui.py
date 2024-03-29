# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BikeStoreMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BikeStoreMainWin(object):
    def setupUi(self, BikeStoreMainWin):
        BikeStoreMainWin.setObjectName("BikeStoreMainWin")
        BikeStoreMainWin.resize(379, 528)
        BikeStoreMainWin.setStyleSheet("background-color: rgb(25, 90, 189);\n"
"color: rgb(255,255,255);")
        self.label_4 = QtWidgets.QLabel(BikeStoreMainWin)
        self.label_4.setGeometry(QtCore.QRect(60, 30, 251, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/icons/logo_main_alt-1.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(BikeStoreMainWin)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 230, 64, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.layoutWidget_2 = QtWidgets.QWidget(BikeStoreMainWin)
        self.layoutWidget_2.setGeometry(QtCore.QRect(90, 220, 258, 141))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtUserName = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtUserName.setMaximumSize(QtCore.QSize(250, 40))
        self.txtUserName.setObjectName("txtUserName")
        self.verticalLayout_2.addWidget(self.txtUserName)
        self.txtPass = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtPass.setMaximumSize(QtCore.QSize(250, 40))
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setObjectName("txtPass")
        self.verticalLayout_2.addWidget(self.txtPass)
        self.layoutWidget_3 = QtWidgets.QWidget(BikeStoreMainWin)
        self.layoutWidget_3.setGeometry(QtCore.QRect(70, 380, 281, 101))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnLogin = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btnLogin.setObjectName("btnLogin")
        self.verticalLayout_3.addWidget(self.btnLogin)
        self.lblLoginError = QtWidgets.QLabel(self.layoutWidget_3)
        self.lblLoginError.setStyleSheet("color: rgb(255, 59, 43);")
        self.lblLoginError.setText("")
        self.lblLoginError.setObjectName("lblLoginError")
        self.verticalLayout_3.addWidget(self.lblLoginError)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnForgetPass = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btnForgetPass.setObjectName("btnForgetPass")
        self.horizontalLayout.addWidget(self.btnForgetPass)
        self.btnSignUp = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btnSignUp.setObjectName("btnSignUp")
        self.horizontalLayout.addWidget(self.btnSignUp)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(BikeStoreMainWin)
        QtCore.QMetaObject.connectSlotsByName(BikeStoreMainWin)

    def retranslateUi(self, BikeStoreMainWin):
        _translate = QtCore.QCoreApplication.translate
        BikeStoreMainWin.setWindowTitle(_translate("BikeStoreMainWin", "Terra Bikes"))
        self.label.setText(_translate("BikeStoreMainWin", "Username"))
        self.label_2.setText(_translate("BikeStoreMainWin", "Password"))
        self.btnLogin.setText(_translate("BikeStoreMainWin", "Login"))
        self.btnForgetPass.setText(_translate("BikeStoreMainWin", "Forgot Password"))
        self.btnSignUp.setText(_translate("BikeStoreMainWin", "Sign Up"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BikeStoreMainWin = QtWidgets.QDialog()
    ui = Ui_BikeStoreMainWin()
    ui.setupUi(BikeStoreMainWin)
    BikeStoreMainWin.show()
    sys.exit(app.exec_())
