# if there is any error check Email_sender , Email_reciever , Email_sender_password .
# this app required that you set up a Gmail account for development



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib, ssl
port = 587
smtp_server = "smtp.gmail.com"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 0, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.situationtext = QtWidgets.QLabel(self.centralwidget)
        self.situationtext.setGeometry(QtCore.QRect(490, 140, 201, 101))
        self.situationtext.setObjectName("situationtext")
        self.situationtext.hide()
        self.emailtext = QtWidgets.QTextEdit(self.centralwidget)
        self.emailtext.setGeometry(QtCore.QRect(150, 140, 151, 41))
        self.emailtext.setObjectName("emailtext")
        self.passwordtext = QtWidgets.QTextEdit(self.centralwidget)
        self.passwordtext.setGeometry(QtCore.QRect(150, 210, 151, 41))
        self.passwordtext.setObjectName("passwordtext")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Old Antic Outline Shaded")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Old Antic Outline Shaded")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.subjecttext = QtWidgets.QTextEdit(self.centralwidget)
        self.subjecttext.setGeometry(QtCore.QRect(100, 310, 171, 51))
        self.subjecttext.setObjectName("subjecttext")
        self.contenttext = QtWidgets.QTextEdit(self.centralwidget)
        self.contenttext.setGeometry(QtCore.QRect(380, 290, 401, 191))
        self.contenttext.setObjectName("contenttext")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Old Antic Outline Shaded")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 320, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Old Antic Outline Shaded")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(340, 500, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName("sendButton")
        self.sendButton.clicked.connect(self.manage_details)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Old Antic Outline Shaded")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.recvmailtext = QtWidgets.QTextEdit(self.centralwidget)
        self.recvmailtext.setGeometry(QtCore.QRect(150, 70, 151, 41))
        self.recvmailtext.setObjectName("recvmailtext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def manage_details(self):
    ## if send button clicked ------ > 
        self.situationtext.hide()
        self.recv_email = self.recvmailtext.toPlainText()
        self.sender_email=self.emailtext.toPlainText()
        self.sender_password=self.passwordtext.toPlainText()
        self.subject_detail=self.subjecttext.toPlainText()
        self.content_detail=self.contenttext.toPlainText()
        self.message = "Subject: "+ self.subject_detail+ "\n \n" + self.content_detail
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  
                server.starttls(context=context)
                server.ehlo()  
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, self.recv_email, self.message)
                self.subjecttext.clear()
                self.contenttext.clear()
                self.situationtext.setText("Email Sent successfully")
                self.situationtext.show()
        except Exception as e:
            print(e)
            self.situationtext.setText("Some error occured - check inputs")
            self.situationtext.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Email Sender"))
        self.situationtext.setText(_translate("MainWindow", "Currently situation"))
        self.label_2.setText(_translate("MainWindow", "Email:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.label_6.setText(_translate("MainWindow", "Subject"))
        self.label_7.setText(_translate("MainWindow", "Content"))
        self.sendButton.setText(_translate("MainWindow", "Send "))
        self.label_4.setText(_translate("MainWindow", "Send to"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
