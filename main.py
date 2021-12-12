from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QMessageBox)
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMenuBar
from gui.login import Ui_login
from gui.inicio import Ui_menu
from banco.model_db import Model_db

import sys


# -> PySide6.QtWidgets.QMenuBar:


class Login(QWidget, Ui_login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")

        # Ação do botão logar
        self.btn_acesso.clicked.connect(self.abrir_sistema)

        # Iniciando a tela de login e "validando os campos"

    def abrir_sistema(self):
        if self.txt_senha.text() == "123" and self.txt_usuario.text() == 'admin':
            self.w = InicioHome()
            self.w.show()
            self.close()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("Usuário ou senha invávlidos")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()


class InicioHome(QMainWindow, Ui_menu):
    def __init__(self):
        super(InicioHome, self).__init__()

        self.setupUi(self)
        self.setWindowTitle('Speak Now - Sistema Multifuncional')
        # appIcon = QIcon('')

        # def menuBar(self, QMenubar):

        # definindo açoes da barra de Menu
        self.pushButton_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_home))
        self.pushButton_listas_alunos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pg_listas_alunos))
        self.pushButton_listas_professores.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pg_listas_professores))
        self.pushButton_listas_cursos_2.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pg_listas_interessados))
        self.pushButton_listas_usuarios.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pg_listas_funcionarios))
        self.pushButton_cadastro_alunos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pg_cadastro_alunos))
        self.pushButton_listas_cursos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pg_listas_impressao))

        # Cadastrar aluno
        self.btn_cadastrar_aluno.clicked.connect(self.aluno_cadastrar)

    def aluno_cadastrar(self):
        # pegando os dados da Tela de Cadastro
        sql = Model_db()

        view_nome = self.txt_nome.text()
        view_cpf = self.txt_cpf.text()
        view_cb_curso = self.cb_curso
        view_telefone = self.txt_telefone.text()
        view_email = self.txt_email.text()
        view_cb_semestre = self.cb_semestre

        # Inserindo dadso no banco de dados
        if view_nome == "" or view_cpf == "" or view_telefone == "" or view_email == "" or view_cb_curso == "" or view_cb_semestre == "":
            QMessageBox.Information(QMessageBox(), "Preencha todos so compos")
        else:
            sql.execute(
                "INSERT INTO alunos (nome, cpf, telefone, curso, matricula, semestre, status) VALUES ('{}', '{}', '{}', '{}', 2603-5, 2009.2, 'Concluído')".format(
                    view_nome, view_cpf, view_cb_curso, view_telefone, view_email, view_cb_semestre))
            QMessageBox.Information(QMessageBox(), "Aluno inserido com sucesso!")

    def limparCampos_AlunosCadastrar(self):
        view_nome = self.stackedWidget.setCurrentWidget(self.txt_nome.setText(''))
        view_cpf = self.stackedWidget.setCurrentWidget(self.txt_cpf.setText(''))
        view_telefone = self.stackedWidget.setCurrentWidget(self.txt_telefone.setText(''))
        view_curso = self.stackedWidget.setCurrentWidget(self.cb_curso.setText(''))
        view_email = self.stackedWidget.setCurrentWidget(self.txt_email.setText(''))
        view_semestre = self.stackedWidget.setCurrentWidget(self.cb_semestre.setText(''))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Login()
    w.show()
    app.exec()
