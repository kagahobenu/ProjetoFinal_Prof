# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicio.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QWidget)
#import inicio_rc

class Ui_menu(object):
    def setupUi(self, menu):
        if not menu.objectName():
            menu.setObjectName(u"menu")
        menu.resize(960, 600)
        menu.setMinimumSize(QSize(960, 600))
        menu.setMaximumSize(QSize(960, 600))
        menu.setSizeIncrement(QSize(960, 600))
        menu.setBaseSize(QSize(960, 600))
        font = QFont()
        font.setBold(True)
        menu.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../.designer/REPERT\u00d3RIO/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        menu.setWindowIcon(icon)
        menu.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        self.centralwidget = QWidget(menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget.setMouseTracking(False)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setEnabled(True)
        self.content.setMinimumSize(QSize(210, 23))
        self.content.setMaximumSize(QSize(65, 16777215))
        self.content.setBaseSize(QSize(3, 0))
        self.content.setStyleSheet(u"background-color: rgb(0, 0, 112);")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.content)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 140, 70))
        self.frame.setMinimumSize(QSize(140, 70))
        self.frame.setMaximumSize(QSize(140, 70))
        self.frame.setSizeIncrement(QSize(140, 70))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-image: url(:/img/logo_menu.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.content)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 110, 171, 431))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_home = QPushButton(self.frame_2)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setGeometry(QRect(0, 0, 161, 24))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        self.pushButton_home.setFont(font1)
        self.pushButton_home.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(237, 224, 7);\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_listas = QPushButton(self.frame_2)
        self.pushButton_listas.setObjectName(u"pushButton_listas")
        self.pushButton_listas.setGeometry(QRect(0, 50, 161, 24))
        self.pushButton_listas.setFont(font1)
        self.pushButton_listas.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_listas.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(237, 224, 7);\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_listas_alunos = QPushButton(self.frame_2)
        self.pushButton_listas_alunos.setObjectName(u"pushButton_listas_alunos")
        self.pushButton_listas_alunos.setGeometry(QRect(0, 80, 161, 24))
        self.pushButton_listas_alunos.setFont(font1)
        self.pushButton_listas_alunos.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_listas_professores = QPushButton(self.frame_2)
        self.pushButton_listas_professores.setObjectName(u"pushButton_listas_professores")
        self.pushButton_listas_professores.setGeometry(QRect(0, 110, 161, 24))
        self.pushButton_listas_professores.setFont(font1)
        self.pushButton_listas_professores.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_listas_cursos = QPushButton(self.frame_2)
        self.pushButton_listas_cursos.setObjectName(u"pushButton_listas_cursos")
        self.pushButton_listas_cursos.setGeometry(QRect(0, 140, 161, 24))
        self.pushButton_listas_cursos.setFont(font1)
        self.pushButton_listas_cursos.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_listas_usuarios = QPushButton(self.frame_2)
        self.pushButton_listas_usuarios.setObjectName(u"pushButton_listas_usuarios")
        self.pushButton_listas_usuarios.setGeometry(QRect(0, 200, 161, 24))
        self.pushButton_listas_usuarios.setFont(font1)
        self.pushButton_listas_usuarios.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_cadastro = QPushButton(self.frame_2)
        self.pushButton_cadastro.setObjectName(u"pushButton_cadastro")
        self.pushButton_cadastro.setGeometry(QRect(0, 240, 161, 24))
        self.pushButton_cadastro.setFont(font1)
        self.pushButton_cadastro.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(237, 224, 7);\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_cadastro_alunos = QPushButton(self.frame_2)
        self.pushButton_cadastro_alunos.setObjectName(u"pushButton_cadastro_alunos")
        self.pushButton_cadastro_alunos.setGeometry(QRect(0, 270, 161, 24))
        self.pushButton_cadastro_alunos.setFont(font1)
        self.pushButton_cadastro_alunos.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.pushButton_cadastro_professores = QPushButton(self.frame_2)
        self.pushButton_cadastro_professores.setObjectName(u"pushButton_cadastro_professores")
        self.pushButton_cadastro_professores.setGeometry(QRect(0, 300, 161, 24))
        self.pushButton_cadastro_professores.setFont(font1)
        self.pushButton_cadastro_professores.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid rgb(37, 104, 191);\n"
"	border-radius: 10px;\n"
"	color: rgb(37, 104, 191);\n"
"}")
        self.pushButton_cadastro_cursos = QPushButton(self.frame_2)
        self.pushButton_cadastro_cursos.setObjectName(u"pushButton_cadastro_cursos")
        self.pushButton_cadastro_cursos.setGeometry(QRect(0, 330, 161, 24))
        self.pushButton_cadastro_cursos.setFont(font1)
        self.pushButton_cadastro_cursos.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid rgb(37, 104, 191);\n"
"	border-radius: 10px;\n"
"	color: rgb(37, 104, 191);\n"
"}")
        self.pushButton_cadastro_usuarios = QPushButton(self.frame_2)
        self.pushButton_cadastro_usuarios.setObjectName(u"pushButton_cadastro_usuarios")
        self.pushButton_cadastro_usuarios.setGeometry(QRect(0, 360, 161, 24))
        self.pushButton_cadastro_usuarios.setFont(font1)
        self.pushButton_cadastro_usuarios.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid rgb(37, 104, 191);\n"
"	border-radius: 10px;\n"
"	color: rgb(37, 104, 191);\n"
"}")
        self.pushButton_cadastro_2 = QPushButton(self.frame_2)
        self.pushButton_cadastro_2.setObjectName(u"pushButton_cadastro_2")
        self.pushButton_cadastro_2.setGeometry(QRect(0, 400, 161, 24))
        self.pushButton_cadastro_2.setFont(font1)
        self.pushButton_cadastro_2.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(37, 104, 191);\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid rgb(37, 104, 191);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"")
        self.pushButton_listas_cursos_2 = QPushButton(self.frame_2)
        self.pushButton_listas_cursos_2.setObjectName(u"pushButton_listas_cursos_2")
        self.pushButton_listas_cursos_2.setGeometry(QRect(0, 170, 161, 24))
        self.pushButton_listas_cursos_2.setFont(font1)
        self.pushButton_listas_cursos_2.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border: 2px solid #ede007 ;\n"
"	border-radius: 10px;\n"
"	color: rgb(237, 224, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(237, 224, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.btn_deslogar = QFrame(self.content)
        self.btn_deslogar.setObjectName(u"btn_deslogar")
        self.btn_deslogar.setGeometry(QRect(10, 550, 31, 41))
        self.btn_deslogar.setStyleSheet(u"QFrame {	\n"
"	background-image: url(:/menu_img/menu_deslogar.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}")
        self.btn_deslogar.setFrameShape(QFrame.StyledPanel)
        self.btn_deslogar.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.content)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 560, 71, 24))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: normal;\n"
"	background-color: rgb(0, 0, 112);\n"
"	color: rgb(237, 224, 7);\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout.addWidget(self.content)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 230, 341, 81))
        self.label.setStyleSheet(u"QLabel {\n"
"	font: 30px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.stackedWidget.addWidget(self.pg_home)
        self.pg_listas_alunos = QWidget()
        self.pg_listas_alunos.setObjectName(u"pg_listas_alunos")
        self.label_2 = QLabel(self.pg_listas_alunos)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 12, 111, 31))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: normal;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.tableWidget = QTableWidget(self.pg_listas_alunos)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 110, 701, 471))
        self.label_10 = QLabel(self.pg_listas_alunos)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 60, 271, 31))
        self.label_10.setStyleSheet(u"QLabel {\n"
"	font: 25px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.stackedWidget.addWidget(self.pg_listas_alunos)
        self.pg_listas_professores = QWidget()
        self.pg_listas_professores.setObjectName(u"pg_listas_professores")
        self.tableWidget_2 = QTableWidget(self.pg_listas_professores)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(30, 110, 701, 451))
        self.label_11 = QLabel(self.pg_listas_professores)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 60, 331, 31))
        self.label_11.setStyleSheet(u"QLabel {\n"
"	font: 25px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.label_3 = QLabel(self.pg_listas_professores)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 12, 151, 31))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: normal;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.stackedWidget.addWidget(self.pg_listas_professores)
        self.pg_listas_impressao = QWidget()
        self.pg_listas_impressao.setObjectName(u"pg_listas_impressao")
        self.label_12 = QLabel(self.pg_listas_impressao)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 60, 351, 31))
        self.label_12.setStyleSheet(u"QLabel {\n"
"	font: 25px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.label_4 = QLabel(self.pg_listas_impressao)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 12, 151, 31))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: normal;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.label_16 = QLabel(self.pg_listas_impressao)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 160, 351, 31))
        self.label_16.setStyleSheet(u"QLabel {\n"
"	font: 25px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 127);\n"
"	background-color: rgb(255, 255, 127);\n"
"}")
        self.stackedWidget.addWidget(self.pg_listas_impressao)
        self.pg_listas_interessados = QWidget()
        self.pg_listas_interessados.setObjectName(u"pg_listas_interessados")
        self.tableWidget_3 = QTableWidget(self.pg_listas_interessados)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(30, 110, 691, 451))
        self.label_9 = QLabel(self.pg_listas_interessados)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 12, 151, 31))
        self.label_9.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: normal;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.label_13 = QLabel(self.pg_listas_interessados)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 60, 401, 31))
        self.label_13.setStyleSheet(u"QLabel {\n"
"	font: 25px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.stackedWidget.addWidget(self.pg_listas_interessados)
        self.pg_listas_funcionarios = QWidget()
        self.pg_listas_funcionarios.setObjectName(u"pg_listas_funcionarios")
        self.tableWidget_4 = QTableWidget(self.pg_listas_funcionarios)
        if (self.tableWidget_4.columnCount() < 6):
            self.tableWidget_4.setColumnCount(6)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(30, 110, 691, 451))
        self.label_14 = QLabel(self.pg_listas_funcionarios)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 12, 151, 31))
        self.label_14.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: normal;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.label_15 = QLabel(self.pg_listas_funcionarios)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 60, 341, 31))
        self.label_15.setStyleSheet(u"QLabel {\n"
"	font: 25px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.stackedWidget.addWidget(self.pg_listas_funcionarios)
        self.pg_cadastro_alunos = QWidget()
        self.pg_cadastro_alunos.setObjectName(u"pg_cadastro_alunos")
        self.label_17 = QLabel(self.pg_cadastro_alunos)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 290, 61, 19))
        self.label_17.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.label_18 = QLabel(self.pg_cadastro_alunos)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 160, 47, 19))
        self.label_18.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.label_19 = QLabel(self.pg_cadastro_alunos)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 220, 51, 19))
        self.label_19.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.label_20 = QLabel(self.pg_cadastro_alunos)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(330, 290, 91, 19))
        self.label_20.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.label_8 = QLabel(self.pg_cadastro_alunos)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 100, 141, 19))
        self.label_8.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.txt_nome = QLineEdit(self.pg_cadastro_alunos)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(40, 120, 501, 31))
        self.txt_nome.setStyleSheet(u"QLineEdit {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.txt_telefone = QLineEdit(self.pg_cadastro_alunos)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setGeometry(QRect(300, 180, 241, 31))
        self.txt_telefone.setStyleSheet(u"QLineEdit {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.btn_cancelar_aluno = QPushButton(self.pg_cadastro_alunos)
        self.btn_cancelar_aluno.setObjectName(u"btn_cancelar_aluno")
        self.btn_cancelar_aluno.setGeometry(QRect(304, 420, 111, 41))
        self.btn_cancelar_aluno.setStyleSheet(u"QPushButton {\n"
"	background-color:  rgb(255, 82, 85);\n"
"	font: 9pt \"Segoe UI\";\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"    color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(187, 237, 6);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.btn_cadastrar_aluno = QPushButton(self.pg_cadastro_alunos)
        self.btn_cadastrar_aluno.setObjectName(u"btn_cadastrar_aluno")
        self.btn_cadastrar_aluno.setGeometry(QRect(440, 420, 111, 41))
        self.btn_cadastrar_aluno.setStyleSheet(u"QPushButton {\n"
"	background-color:  rgb(131, 255, 156);\n"
"\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"	font: 8pt \"Segoe UI Historic\";\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(187, 237, 6);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 214, 4);\n"
"}")
        self.cb_curso = QComboBox(self.pg_cadastro_alunos)
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.setObjectName(u"cb_curso")
        self.cb_curso.setGeometry(QRect(40, 310, 241, 31))
        self.cb_curso.setStyleSheet(u"QComboBox {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 2px solid grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"     background: white;\n"
" }")
        self.txt_cpf = QLineEdit(self.pg_cadastro_alunos)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setGeometry(QRect(40, 180, 241, 31))
        self.txt_cpf.setStyleSheet(u"QLineEdit {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.label_5 = QLabel(self.pg_cadastro_alunos)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 20, 341, 41))
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font: 35px Montserrat, sans-serif;\n"
"	font-weight: normal;\n"
"	color: rgb(0, 0, 112);\n"
"}\n"
"\n"
"")
        self.txt_email = QLineEdit(self.pg_cadastro_alunos)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(40, 240, 501, 31))
        self.txt_email.setStyleSheet(u"QLineEdit {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.label_21 = QLabel(self.pg_cadastro_alunos)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(310, 160, 81, 19))
        self.label_21.setStyleSheet(u"QLabel {\n"
"	font: 15px Montserrat, sans-serif;\n"
"	font-weight: bold;\n"
"	color: rgb(0, 0, 112);\n"
"	border: 0px;\n"
"}\n"
"")
        self.cb_semestre = QComboBox(self.pg_cadastro_alunos)
        self.cb_semestre.addItem("")
        self.cb_semestre.addItem("")
        self.cb_semestre.addItem("")
        self.cb_semestre.addItem("")
        self.cb_semestre.setObjectName(u"cb_semestre")
        self.cb_semestre.setGeometry(QRect(310, 310, 241, 31))
        self.cb_semestre.setStyleSheet(u"QComboBox {	\n"
"	border: 2px solid #000070 ;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 2px solid grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"     background: white;\n"
" }")
        self.stackedWidget.addWidget(self.pg_cadastro_alunos)

        self.horizontalLayout.addWidget(self.stackedWidget)

        menu.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.txt_nome, self.txt_cpf)
        QWidget.setTabOrder(self.txt_cpf, self.txt_telefone)
        QWidget.setTabOrder(self.txt_telefone, self.txt_email)
        QWidget.setTabOrder(self.txt_email, self.cb_curso)
        QWidget.setTabOrder(self.cb_curso, self.cb_semestre)
        QWidget.setTabOrder(self.cb_semestre, self.btn_cadastrar_aluno)
        QWidget.setTabOrder(self.btn_cadastrar_aluno, self.btn_cancelar_aluno)
        QWidget.setTabOrder(self.btn_cancelar_aluno, self.pushButton_cadastro_professores)
        QWidget.setTabOrder(self.pushButton_cadastro_professores, self.pushButton_cadastro_cursos)
        QWidget.setTabOrder(self.pushButton_cadastro_cursos, self.pushButton_cadastro_usuarios)
        QWidget.setTabOrder(self.pushButton_cadastro_usuarios, self.pushButton_cadastro_2)
        QWidget.setTabOrder(self.pushButton_cadastro_2, self.pushButton_listas_cursos_2)
        QWidget.setTabOrder(self.pushButton_listas_cursos_2, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.tableWidget_2)
        QWidget.setTabOrder(self.tableWidget_2, self.tableWidget_3)
        QWidget.setTabOrder(self.tableWidget_3, self.tableWidget_4)
        QWidget.setTabOrder(self.tableWidget_4, self.pushButton_home)
        QWidget.setTabOrder(self.pushButton_home, self.pushButton_listas_alunos)
        QWidget.setTabOrder(self.pushButton_listas_alunos, self.pushButton_cadastro_alunos)
        QWidget.setTabOrder(self.pushButton_cadastro_alunos, self.pushButton_cadastro)
        QWidget.setTabOrder(self.pushButton_cadastro, self.pushButton_listas_cursos)
        QWidget.setTabOrder(self.pushButton_listas_cursos, self.pushButton_listas)
        QWidget.setTabOrder(self.pushButton_listas, self.pushButton_listas_professores)
        QWidget.setTabOrder(self.pushButton_listas_professores, self.pushButton_listas_usuarios)

        self.retranslateUi(menu)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(menu)
    # setupUi

    def retranslateUi(self, menu):
        menu.setWindowTitle(QCoreApplication.translate("menu", u"speak now - menu", None))
        self.pushButton_home.setText(QCoreApplication.translate("menu", u"Home", None))
        self.pushButton_listas.setText(QCoreApplication.translate("menu", u"Listas", None))
        self.pushButton_listas_alunos.setText(QCoreApplication.translate("menu", u"Alunos", None))
        self.pushButton_listas_professores.setText(QCoreApplication.translate("menu", u"Professores", None))
        self.pushButton_listas_cursos.setText(QCoreApplication.translate("menu", u"Impress\u00e3o", None))
        self.pushButton_listas_usuarios.setText(QCoreApplication.translate("menu", u"Funcion\u00e1rios", None))
        self.pushButton_cadastro.setText(QCoreApplication.translate("menu", u"Cadastro", None))
        self.pushButton_cadastro_alunos.setText(QCoreApplication.translate("menu", u"Alunos", None))
        self.pushButton_cadastro_professores.setText(QCoreApplication.translate("menu", u"Professores", None))
        self.pushButton_cadastro_cursos.setText(QCoreApplication.translate("menu", u"Cursos", None))
        self.pushButton_cadastro_usuarios.setText(QCoreApplication.translate("menu", u"Usu\u00e1rios", None))
        self.pushButton_cadastro_2.setText(QCoreApplication.translate("menu", u"Relat\u00f3rios", None))
        self.pushButton_listas_cursos_2.setText(QCoreApplication.translate("menu", u"Interessados", None))
        self.pushButton.setText(QCoreApplication.translate("menu", u"Deslogar", None))
        self.label.setText(QCoreApplication.translate("menu", u"Bem-vindo(a)!", None))
        self.label_2.setText(QCoreApplication.translate("menu", u"Listas/ alunos", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("menu", u"NOME", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("menu", u"CPF", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("menu", u"TELEFONE", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("menu", u"CURSO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("menu", u"MATRICULA", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("menu", u"SEMESTRE", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("menu", u"STATUS", None));
        self.label_10.setText(QCoreApplication.translate("menu", u"Informa\u00e7\u00f5es alunos", None))
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("menu", u"NOME", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("menu", u"CPF", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("menu", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("menu", u"CURSO", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("menu", u"MATRICULA", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("menu", u"QUANT.", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("menu", u"STATUS", None));
        self.label_11.setText(QCoreApplication.translate("menu", u"Informa\u00e7\u00f5es professores", None))
        self.label_3.setText(QCoreApplication.translate("menu", u"Listas/ professores", None))
        self.label_12.setText(QCoreApplication.translate("menu", u"Informa\u00e7\u00f5es de impress\u00e3o", None))
        self.label_4.setText(QCoreApplication.translate("menu", u"Listas/ impress\u00e3o", None))
        self.label_16.setText(QCoreApplication.translate("menu", u"<html><head/><body><p align=\"center\"><span style=\" font-size:19pt;\">Pop-ups de impress\u00e3o</span></p></body></html>", None))
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("menu", u"NOME", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("menu", u"CPF", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("menu", u"TELEFONE", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("menu", u"CURSO", None));
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("menu", u"STATUS", None));
        self.label_9.setText(QCoreApplication.translate("menu", u"Listas/ interessados", None))
        self.label_13.setText(QCoreApplication.translate("menu", u"Informa\u00e7\u00f5es de interessados", None))
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("menu", u"NOME", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("menu", u"CPF", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("menu", u"TELEFONE", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("menu", u"MATRICULA", None));
        ___qtablewidgetitem23 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("menu", u"FUN\u00c7\u00c3O", None));
        ___qtablewidgetitem24 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("menu", u"CARGO", None));
        self.label_14.setText(QCoreApplication.translate("menu", u"Listas/ funcion\u00e1rios", None))
        self.label_15.setText(QCoreApplication.translate("menu", u"Informa\u00e7\u00f5es funcion\u00e1rios", None))
        self.label_17.setText(QCoreApplication.translate("menu", u"CURSO", None))
        self.label_18.setText(QCoreApplication.translate("menu", u"CPF", None))
        self.label_19.setText(QCoreApplication.translate("menu", u"EMAIL", None))
        self.label_20.setText(QCoreApplication.translate("menu", u"SEMESTRE", None))
        self.label_8.setText(QCoreApplication.translate("menu", u"NOME COMPLETO", None))
        self.btn_cancelar_aluno.setText(QCoreApplication.translate("menu", u"CANCELAR", None))
        self.btn_cadastrar_aluno.setText(QCoreApplication.translate("menu", u"CADASTRAR", None))
        self.cb_curso.setItemText(0, QCoreApplication.translate("menu", u"Ingl\u00eas", None))
        self.cb_curso.setItemText(1, QCoreApplication.translate("menu", u"Espanhol", None))
        self.cb_curso.setItemText(2, QCoreApplication.translate("menu", u"Franc\u00eas", None))
        self.cb_curso.setItemText(3, QCoreApplication.translate("menu", u"Alem\u00e3o", None))

        self.label_5.setText(QCoreApplication.translate("menu", u"Cadastro > alunos", None))
        self.label_21.setText(QCoreApplication.translate("menu", u"TELEFONE", None))
        self.cb_semestre.setItemText(0, QCoreApplication.translate("menu", u"Ingl\u00eas", None))
        self.cb_semestre.setItemText(1, QCoreApplication.translate("menu", u"Espanhol", None))
        self.cb_semestre.setItemText(2, QCoreApplication.translate("menu", u"Franc\u00eas", None))
        self.cb_semestre.setItemText(3, QCoreApplication.translate("menu", u"Alem\u00e3o", None))

    # retranslateUi

