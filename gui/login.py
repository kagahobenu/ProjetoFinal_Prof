# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(670, 586)
        login.setStyleSheet(u"")
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 671, 51))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_usi = QFrame(self.frame)
        self.txt_usi.setObjectName(u"txt_usi")
        self.txt_usi.setGeometry(QRect(200, 10, 251, 31))
        self.txt_usi.setStyleSheet(u"background-color: #ede007;\n"
"border-radius: 15px;")
        self.txt_usi.setFrameShape(QFrame.StyledPanel)
        self.txt_usi.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.txt_usi)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.txt_usi)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 112);")

        self.horizontalLayout.addWidget(self.label)

        self.btn_erro = QPushButton(self.txt_usi)
        self.btn_erro.setObjectName(u"btn_erro")
        self.btn_erro.setStyleSheet(u"font: 700 italic 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.btn_erro)

        self.content = QFrame(login)
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(-10, 50, 681, 541))
        self.content.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.login_area = QFrame(self.content)
        self.login_area.setObjectName(u"login_area")
        self.login_area.setGeometry(QRect(150, 9, 401, 511))
        self.login_area.setStyleSheet(u"background-color: rgb(0, 0, 112);")
        self.login_area.setFrameShape(QFrame.StyledPanel)
        self.login_area.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.login_area)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(90, 50, 221, 101))
        self.frame_3.setStyleSheet(u"image: url(:/newPrefix/logo_login.png);")
        self.txt_usuario = QLineEdit(self.login_area)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(70, 190, 280, 41))
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}")
        self.txt_usuario.setAlignment(Qt.AlignCenter)
        self.txt_senha = QLineEdit(self.login_area)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(70, 240, 280, 41))
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)
        self.checkBox = QCheckBox(self.login_area)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(80, 290, 131, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.checkBox.setFont(font1)
        self.checkBox.setFocusPolicy(Qt.WheelFocus)
        self.checkBox.setStyleSheet(u"QCheckBox  {\n"
"	color: rgb(237, 224, 7)\n"
"}\n"
"\n"
"QCheckBox:indicator  {\n"
"	border: 1px solid rgb(237, 224, 7);\n"
"	border-radius: 3px;\n"
"	width: 12px;	\n"
"	height: 12px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked  {\n"
"	border: 1px solid rgb(237, 224, 7);\n"
"	background-color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.btn_acesso = QPushButton(self.login_area)
        self.btn_acesso.setObjectName(u"btn_acesso")
        self.btn_acesso.setGeometry(QRect(70, 320, 280, 41))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(True)
        self.btn_acesso.setFont(font2)
        self.btn_acesso.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(187, 237, 6);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.txt_usuario.raise_()
        self.txt_senha.raise_()
        self.checkBox.raise_()
        self.btn_acesso.raise_()
        self.frame_3.raise_()

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.label.setText(QCoreApplication.translate("login", u"Usu\u00e1rio ou senha inv\u00e1lida.", None))
        self.btn_erro.setText(QCoreApplication.translate("login", u"X", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("login", u"usu\u00e1rio", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("login", u"senha", None))
        self.checkBox.setText(QCoreApplication.translate("login", u"lembrar usu\u00e1rio", None))
        self.btn_acesso.setText(QCoreApplication.translate("login", u"acessar", None))
    # retranslateUi

