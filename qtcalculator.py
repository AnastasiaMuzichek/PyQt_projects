# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(399, 431)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_resuit = QtWidgets.QLabel(self.centralwidget)
        self.label_resuit.setGeometry(QtCore.QRect(0, -1, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Plantagenet Cherokee")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_resuit.setFont(font)
        self.label_resuit.setStyleSheet("color: rgb(7, 7, 7);\n"
"border-color: rgb(0, 177, 177);\n"
"background-color: rgb(193, 193, 193);\npadding-left: 15px;")
        self.label_resuit.setObjectName("label_resuit")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 70, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(18, 195, 166);\n"
"")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 70, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(18, 195, 166);\n"
"")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 70, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(18, 195, 166);\n"
"")
        self.btn_9.setObjectName("btn_9")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 150, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(18, 195, 166);\n"
"")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 150, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(18, 195, 166);\n"
"")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 150, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(18, 195, 166);\n"
"")
        self.btn_6.setObjectName("btn_6")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 230, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(18, 195, 166);\n"
"")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 230, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(18, 195, 166);\n"
"")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 230, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(18, 195, 166);\n"
"")
        self.btn_3.setObjectName("btn_3")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(300, 70, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.plus.setFont(font)
        self.plus.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(68, 195, 220);\n"
"")
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(300, 150, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.minus.setFont(font)
        self.minus.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(68, 195, 220);\n"
"")
        self.minus.setObjectName("minus")
        self.umno = QtWidgets.QPushButton(self.centralwidget)
        self.umno.setGeometry(QtCore.QRect(300, 230, 100, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.umno.setFont(font)
        self.umno.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(68, 195, 220);\n"
"")
        self.umno.setObjectName("umno")
        self.delenie = QtWidgets.QPushButton(self.centralwidget)
        self.delenie.setGeometry(QtCore.QRect(299, 310, 101, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.delenie.setFont(font)
        self.delenie.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(68, 195, 220);\n"
"")
        self.delenie.setObjectName("delenie")
        self.btn_zero = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zero.setGeometry(QtCore.QRect(0, 310, 151, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(18, 195, 166);\n"
"")
        self.btn_zero.setObjectName("btn_zero")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(150, 310, 151, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(105, 145, 255);\n"
"")
        self.btn_equal.setObjectName("btn_equal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_fuctions()

        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????????? ????????-????????"))
        self.label_resuit.setText(_translate("MainWindow", "0"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.plus.setText(_translate("MainWindow", " + "))
        self.minus.setText(_translate("MainWindow", " - "))
        self.umno.setText(_translate("MainWindow", " * "))
        self.delenie.setText(_translate("MainWindow", " / "))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_equal.setText(_translate("MainWindow", "="))

    def add_fuctions(self):
        self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.plus.clicked.connect(lambda: self.write_number(self.plus.text()))
        self.minus.clicked.connect(lambda: self.write_number(self.minus.text()))
        self.umno.clicked.connect(lambda: self.write_number(self.umno.text()))
        self.delenie.clicked.connect(lambda: self.write_number(self.delenie.text()))
        #self.btn_equal.clicked.connect(lambda: self.write_number(self.btn_equal.text()))

        self.btn_equal.clicked.connect(self.results)


    def write_number(self, number):
        if self.label_resuit.text() == "0" or self.is_equal:
            self.label_resuit.setText(number)
            self.is_equal = False
        else:
            self.label_resuit.setText(self.label_resuit.text() + number)


    def results(self):
        try:
            res = eval(self.label_resuit.text())
            self.label_resuit.setText("??????????????????: " + str(res))
            self.is_equal = True
        except Exception:
            error = QMessageBox()
            error.setWindowTitle("????????????")
            error.setText("?????? ???????????????? ?????????????????? ????????????!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Reset |QMessageBox.Ok | QMessageBox.Cancel)
            error.setInformativeText("?????????????????????? ???????????????? ????????????????:(")
            error.setDetailedText("???????????????? ?????? ???? ?????????????????? ???????????? ???? ????????. ?????????????????????? ???????????? ?? ????????????!")

            error.buttonClicked.connect(self.popup_action)

            error.exec()

    def popup_action(self, btn):
        if btn.text() == "Ok":
            print('Print Ok')
        elif btn.text() == "Reset":
            self.label_resuit.setText("")
            self.is_equal = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
