# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinalRod-Calc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 525)
        MainWindow.setMinimumSize(QtCore.QSize(807, 525))
        MainWindow.setMaximumSize(QtCore.QSize(807, 525))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 471, 371))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lin_1 = QtWidgets.QLineEdit(self.groupBox)
        self.lin_1.setGeometry(QtCore.QRect(30, 120, 111, 31))
        self.lin_1.setText("")
        self.lin_1.setFrame(True)
        self.lin_1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lin_1.setClearButtonEnabled(False)
        self.lin_1.setObjectName("lin_1")
        self.com_1 = QtWidgets.QComboBox(self.groupBox)
        self.com_1.setGeometry(QtCore.QRect(350, 120, 91, 31))
        self.com_1.setObjectName("com_1")
        self.com_1.addItem("")
        self.com_1.addItem("")
        self.com_1.addItem("")
        self.com_1.addItem("")
        self.com_1.addItem("")
        self.com_1.addItem("")
        self.com_1.addItem("")
        self.com_2 = QtWidgets.QComboBox(self.groupBox)
        self.com_2.setGeometry(QtCore.QRect(350, 160, 91, 31))
        self.com_2.setObjectName("com_2")
        self.com_2.addItem("")
        self.com_2.addItem("")
        self.com_2.addItem("")
        self.com_2.addItem("")
        self.com_2.addItem("")
        self.com_2.addItem("")
        self.com_2.addItem("")
        self.lin_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lin_2.setGeometry(QtCore.QRect(30, 160, 111, 31))
        self.lin_2.setText("")
        self.lin_2.setObjectName("lin_2")
        self.com_3 = QtWidgets.QComboBox(self.groupBox)
        self.com_3.setGeometry(QtCore.QRect(350, 200, 91, 31))
        self.com_3.setObjectName("com_3")
        self.com_3.addItem("")
        self.com_3.addItem("")
        self.com_3.addItem("")
        self.com_3.addItem("")
        self.com_3.addItem("")
        self.com_3.addItem("")
        self.com_3.addItem("")
        self.lin_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lin_3.setGeometry(QtCore.QRect(30, 200, 111, 31))
        self.lin_3.setText("")
        self.lin_3.setObjectName("lin_3")
        self.com_4 = QtWidgets.QComboBox(self.groupBox)
        self.com_4.setGeometry(QtCore.QRect(350, 240, 91, 31))
        self.com_4.setObjectName("com_4")
        self.com_4.addItem("")
        self.com_4.addItem("")
        self.com_4.addItem("")
        self.com_4.addItem("")
        self.com_4.addItem("")
        self.com_4.addItem("")
        self.com_4.addItem("")
        self.lin_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lin_4.setGeometry(QtCore.QRect(30, 240, 111, 31))
        self.lin_4.setText("")
        self.lin_4.setObjectName("lin_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(100, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lin_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lin_5.setGeometry(QtCore.QRect(30, 280, 111, 31))
        self.lin_5.setText("")
        self.lin_5.setObjectName("lin_5")
        self.com_5 = QtWidgets.QComboBox(self.groupBox)
        self.com_5.setGeometry(QtCore.QRect(350, 280, 91, 31))
        self.com_5.setObjectName("com_5")
        self.com_5.addItem("")
        self.com_5.addItem("")
        self.com_5.addItem("")
        self.com_5.addItem("")
        self.com_5.addItem("")
        self.com_5.addItem("")
        self.com_5.addItem("")
        self.com_7 = QtWidgets.QComboBox(self.groupBox)
        self.com_7.setGeometry(QtCore.QRect(168, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.com_7.setFont(font)
        self.com_7.setObjectName("com_7")
        self.com_7.addItem("")
        self.com_7.addItem("")
        self.com_7.addItem("")
        self.com_7.addItem("")
        self.com_7.addItem("")
        self.com_7.addItem("")
        self.com_7.addItem("")
        self.com_7.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(310, 160, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(310, 200, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(310, 240, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(310, 280, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(310, 320, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.com_8 = QtWidgets.QComboBox(self.groupBox)
        self.com_8.setGeometry(QtCore.QRect(168, 160, 131, 31))
        self.com_8.setObjectName("com_8")
        self.com_8.addItem("")
        self.com_8.addItem("")
        self.com_8.addItem("")
        self.com_8.addItem("")
        self.com_8.addItem("")
        self.com_8.addItem("")
        self.com_8.addItem("")
        self.com_8.addItem("")
        self.com_9 = QtWidgets.QComboBox(self.groupBox)
        self.com_9.setGeometry(QtCore.QRect(168, 200, 131, 31))
        self.com_9.setObjectName("com_9")
        self.com_9.addItem("")
        self.com_9.addItem("")
        self.com_9.addItem("")
        self.com_9.addItem("")
        self.com_9.addItem("")
        self.com_9.addItem("")
        self.com_9.addItem("")
        self.com_9.addItem("")
        self.com_10 = QtWidgets.QComboBox(self.groupBox)
        self.com_10.setGeometry(QtCore.QRect(168, 240, 131, 31))
        self.com_10.setObjectName("com_10")
        self.com_10.addItem("")
        self.com_10.addItem("")
        self.com_10.addItem("")
        self.com_10.addItem("")
        self.com_10.addItem("")
        self.com_10.addItem("")
        self.com_10.addItem("")
        self.com_10.addItem("")
        self.com_11 = QtWidgets.QComboBox(self.groupBox)
        self.com_11.setGeometry(QtCore.QRect(168, 280, 131, 31))
        self.com_11.setObjectName("com_11")
        self.com_11.addItem("")
        self.com_11.addItem("")
        self.com_11.addItem("")
        self.com_11.addItem("")
        self.com_11.addItem("")
        self.com_11.addItem("")
        self.com_11.addItem("")
        self.com_11.addItem("")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 91, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(170, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(350, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(640, 120, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.lin_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lin_6.setGeometry(QtCore.QRect(30, 320, 111, 31))
        self.lin_6.setText("")
        self.lin_6.setObjectName("lin_6")
        self.com_12 = QtWidgets.QComboBox(self.groupBox)
        self.com_12.setGeometry(QtCore.QRect(170, 320, 131, 31))
        self.com_12.setObjectName("com_12")
        self.com_12.addItem("")
        self.com_12.addItem("")
        self.com_12.addItem("")
        self.com_12.addItem("")
        self.com_12.addItem("")
        self.com_12.addItem("")
        self.com_12.addItem("")
        self.com_12.addItem("")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(310, 120, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.com_6 = QtWidgets.QComboBox(self.groupBox)
        self.com_6.setGeometry(QtCore.QRect(350, 320, 91, 31))
        self.com_6.setObjectName("com_6")
        self.com_6.addItem("")
        self.com_6.addItem("")
        self.com_6.addItem("")
        self.com_6.addItem("")
        self.com_6.addItem("")
        self.com_6.addItem("")
        self.com_6.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 90, 271, 371))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lb_btn = QtWidgets.QRadioButton(self.groupBox_2)
        self.lb_btn.setGeometry(QtCore.QRect(30, 100, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lb_btn.setFont(font)
        self.lb_btn.setChecked(True)
        self.lb_btn.setObjectName("lb_btn")
        self.ton_btn = QtWidgets.QRadioButton(self.groupBox_2)
        self.ton_btn.setGeometry(QtCore.QRect(30, 120, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ton_btn.setFont(font)
        self.ton_btn.setObjectName("ton_btn")
        self.calc_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.calc_btn.setGeometry(QtCore.QRect(40, 200, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calc_btn.setFont(font)
        self.calc_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/PROGRAMMING/Images/Icons/calculating.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calc_btn.setIcon(icon)
        self.calc_btn.setIconSize(QtCore.QSize(25, 25))
        self.calc_btn.setAutoDefault(False)
        self.calc_btn.setDefault(True)
        self.calc_btn.setFlat(False)
        self.calc_btn.setObjectName("calc_btn")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(40, 270, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(40, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.buy_btn = QtWidgets.QCheckBox(self.groupBox_2)
        self.buy_btn.setGeometry(QtCore.QRect(110, 100, 131, 21))
        self.buy_btn.setObjectName("buy_btn")
        self.api_btn = QtWidgets.QLineEdit(self.groupBox_2)
        self.api_btn.setGeometry(QtCore.QRect(112, 120, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.api_btn.setFont(font)
        self.api_btn.setAlignment(QtCore.Qt.AlignCenter)
        self.api_btn.setObjectName("api_btn")
        self.unit_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.unit_lbl.setGeometry(QtCore.QRect(210, 300, 31, 51))
        self.unit_lbl.setObjectName("unit_lbl")
        self.lcd = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcd.setGeometry(QtCore.QRect(40, 300, 161, 51))
        self.lcd.setSmallDecimalPoint(False)
        self.lcd.setObjectName("lcd")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 10, 761, 81))
        self.groupBox_3.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 681, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SR Weight Calculator"))
        self.lin_1.setPlaceholderText(_translate("MainWindow", "Taper 1"))
        self.com_1.setItemText(0, _translate("MainWindow", "----"))
        self.com_1.setItemText(1, _translate("MainWindow", "3/4 inch"))
        self.com_1.setItemText(2, _translate("MainWindow", "7/8 inch"))
        self.com_1.setItemText(3, _translate("MainWindow", "1 inch"))
        self.com_1.setItemText(4, _translate("MainWindow", "1 1/8 inch"))
        self.com_1.setItemText(5, _translate("MainWindow", "1 1/4 inch"))
        self.com_1.setItemText(6, _translate("MainWindow", "1 1/2 inch"))
        self.com_2.setItemText(0, _translate("MainWindow", "----"))
        self.com_2.setItemText(1, _translate("MainWindow", "3/4 inch"))
        self.com_2.setItemText(2, _translate("MainWindow", "7/8 inch"))
        self.com_2.setItemText(3, _translate("MainWindow", "1 inch"))
        self.com_2.setItemText(4, _translate("MainWindow", "1 1/8 inch"))
        self.com_2.setItemText(5, _translate("MainWindow", "1 1/4 inch"))
        self.com_2.setItemText(6, _translate("MainWindow", "1 1/2 inch"))
        self.lin_2.setPlaceholderText(_translate("MainWindow", "Taper 2"))
        self.com_3.setItemText(0, _translate("MainWindow", "----"))
        self.com_3.setItemText(1, _translate("MainWindow", "3/4 inch"))
        self.com_3.setItemText(2, _translate("MainWindow", "7/8 inch"))
        self.com_3.setItemText(3, _translate("MainWindow", "1 inch"))
        self.com_3.setItemText(4, _translate("MainWindow", "1 1/8 inch"))
        self.com_3.setItemText(5, _translate("MainWindow", "1 1/4 inch"))
        self.com_3.setItemText(6, _translate("MainWindow", "1 1/2 inch"))
        self.lin_3.setPlaceholderText(_translate("MainWindow", "Taper 3"))
        self.com_4.setItemText(0, _translate("MainWindow", "----"))
        self.com_4.setItemText(1, _translate("MainWindow", "3/4 inch"))
        self.com_4.setItemText(2, _translate("MainWindow", "7/8 inch"))
        self.com_4.setItemText(3, _translate("MainWindow", "1 inch"))
        self.com_4.setItemText(4, _translate("MainWindow", "1 1/8 inch"))
        self.com_4.setItemText(5, _translate("MainWindow", "1 1/4 inch"))
        self.com_4.setItemText(6, _translate("MainWindow", "1 1/2 inch"))
        self.lin_4.setPlaceholderText(_translate("MainWindow", "Taper 4"))
        self.label_4.setText(_translate("MainWindow", "STRING DETAILS"))
        self.lin_5.setPlaceholderText(_translate("MainWindow", "Taper 5"))
        self.com_5.setItemText(0, _translate("MainWindow", "----"))
        self.com_5.setItemText(1, _translate("MainWindow", "3/4 inch"))
        self.com_5.setItemText(2, _translate("MainWindow", "7/8 inch"))
        self.com_5.setItemText(3, _translate("MainWindow", "1 inch"))
        self.com_5.setItemText(4, _translate("MainWindow", "1 1/8 inch"))
        self.com_5.setItemText(5, _translate("MainWindow", "1 1/4 inch"))
        self.com_5.setItemText(6, _translate("MainWindow", "1 1/2 inch"))
        self.com_7.setCurrentText(_translate("MainWindow", "select rod length"))
        self.com_7.setItemText(0, _translate("MainWindow", "select rod length"))
        self.com_7.setItemText(1, _translate("MainWindow", "30"))
        self.com_7.setItemText(2, _translate("MainWindow", "25"))
        self.com_7.setItemText(3, _translate("MainWindow", "10"))
        self.com_7.setItemText(4, _translate("MainWindow", "8"))
        self.com_7.setItemText(5, _translate("MainWindow", "6"))
        self.com_7.setItemText(6, _translate("MainWindow", "4"))
        self.com_7.setItemText(7, _translate("MainWindow", "2"))
        self.label_2.setText(_translate("MainWindow", "ft"))
        self.label_5.setText(_translate("MainWindow", "ft"))
        self.label_6.setText(_translate("MainWindow", "ft"))
        self.label_7.setText(_translate("MainWindow", "ft"))
        self.label_8.setText(_translate("MainWindow", "ft"))
        self.com_8.setItemText(0, _translate("MainWindow", "select rod length"))
        self.com_8.setItemText(1, _translate("MainWindow", "30"))
        self.com_8.setItemText(2, _translate("MainWindow", "25"))
        self.com_8.setItemText(3, _translate("MainWindow", "10"))
        self.com_8.setItemText(4, _translate("MainWindow", "8"))
        self.com_8.setItemText(5, _translate("MainWindow", "6"))
        self.com_8.setItemText(6, _translate("MainWindow", "4"))
        self.com_8.setItemText(7, _translate("MainWindow", "2"))
        self.com_9.setItemText(0, _translate("MainWindow", "select rod length"))
        self.com_9.setItemText(1, _translate("MainWindow", "30"))
        self.com_9.setItemText(2, _translate("MainWindow", "25"))
        self.com_9.setItemText(3, _translate("MainWindow", "10"))
        self.com_9.setItemText(4, _translate("MainWindow", "8"))
        self.com_9.setItemText(5, _translate("MainWindow", "6"))
        self.com_9.setItemText(6, _translate("MainWindow", "4"))
        self.com_9.setItemText(7, _translate("MainWindow", "2"))
        self.com_10.setItemText(0, _translate("MainWindow", "select rod length"))
        self.com_10.setItemText(1, _translate("MainWindow", "30"))
        self.com_10.setItemText(2, _translate("MainWindow", "25"))
        self.com_10.setItemText(3, _translate("MainWindow", "10"))
        self.com_10.setItemText(4, _translate("MainWindow", "8"))
        self.com_10.setItemText(5, _translate("MainWindow", "6"))
        self.com_10.setItemText(6, _translate("MainWindow", "4"))
        self.com_10.setItemText(7, _translate("MainWindow", "2"))
        self.com_11.setItemText(0, _translate("MainWindow", "select rod length"))
        self.com_11.setItemText(1, _translate("MainWindow", "30"))
        self.com_11.setItemText(2, _translate("MainWindow", "25"))
        self.com_11.setItemText(3, _translate("MainWindow", "10"))
        self.com_11.setItemText(4, _translate("MainWindow", "8"))
        self.com_11.setItemText(5, _translate("MainWindow", "6"))
        self.com_11.setItemText(6, _translate("MainWindow", "4"))
        self.com_11.setItemText(7, _translate("MainWindow", "2"))
        self.label_9.setText(_translate("MainWindow", "Number of rods"))
        self.label_10.setText(_translate("MainWindow", "Rod length"))
        self.label_11.setText(_translate("MainWindow", "Size"))
        self.label_12.setText(_translate("MainWindow", "Total string weight"))
        self.lin_6.setPlaceholderText(_translate("MainWindow", "Taper 6"))
        self.com_12.setItemText(0, _translate("MainWindow", "select rod length"))
        self.com_12.setItemText(1, _translate("MainWindow", "30"))
        self.com_12.setItemText(2, _translate("MainWindow", "25"))
        self.com_12.setItemText(3, _translate("MainWindow", "10"))
        self.com_12.setItemText(4, _translate("MainWindow", "8"))
        self.com_12.setItemText(5, _translate("MainWindow", "6"))
        self.com_12.setItemText(6, _translate("MainWindow", "4"))
        self.com_12.setItemText(7, _translate("MainWindow", "2"))
        self.label_15.setText(_translate("MainWindow", "ft"))
        self.com_6.setItemText(0, _translate("MainWindow", "----"))
        self.com_6.setItemText(1, _translate("MainWindow", "3/4 inch"))
        self.com_6.setItemText(2, _translate("MainWindow", "7/8 inch"))
        self.com_6.setItemText(3, _translate("MainWindow", "1 inch"))
        self.com_6.setItemText(4, _translate("MainWindow", "1 1/8 inch"))
        self.com_6.setItemText(5, _translate("MainWindow", "1 1/4 inch"))
        self.com_6.setItemText(6, _translate("MainWindow", "1 1/2 inch"))
        self.lb_btn.setText(_translate("MainWindow", "Klbs"))
        self.ton_btn.setText(_translate("MainWindow", "Tons"))
        self.calc_btn.setText(_translate("MainWindow", "CALCULATE"))
        self.label_13.setText(_translate("MainWindow", "Total rod string weight"))
        self.label_14.setText(_translate("MainWindow", "OUTPUT"))
        self.buy_btn.setText(_translate("MainWindow", "Consider Bouyancy"))
        self.api_btn.setPlaceholderText(_translate("MainWindow", "Fluid  API"))
        self.unit_lbl.setText(_translate("MainWindow", "Klbs"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:400; color:#9e0000;\">SUCKER ROD STRING WEIGHT CALCULATOR</span></p></body></html>"))
