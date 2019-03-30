from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox,QLCDNumber
from PyQt5.uic import loadUi
import qdarkstyle
from PyQt5.uic import loadUiType
from FinalRod_Calc import *


class Calc(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
       #loadUi("E:/codes/My applications/SR-Wt-Calculator/FinalRod-Calc.ui", self)
        self.calc_btn.clicked.connect(self.calc)
        self.show()

    def calc(self):
        lines = [self.lin_1, self.lin_2, self.lin_3, self.lin_4, self.lin_5, self.lin_6]
        sizes = [self.com_1, self.com_2, self.com_3, self.com_4, self.com_5,self.com_6]
        lenghts = [self.com_7, self.com_8, self.com_9, self.com_10,self.com_11,self.com_12]
        zipped = zip(lines, lenghts, sizes)
        total = []
        try:
            for i, k, j in zipped:
                if k.currentText()=="select rod length" or i.text()=="":
                    res=0
                else:
                    if j.currentText() == '3/4 inch':
                        res = (float(i.text()) * float(k.currentText())) * 2.2
                        total.append(res)
                    elif j.currentText() == '7/8 inch':
                        res = (float(i.text()) * float(k.currentText())) * 2.224
                        total.append(res)
                    elif j.currentText() == '1 inch':
                        res = (float(i.text()) * float(k.currentText())) * 2.904
                        total.append(res)
                    elif j.currentText() == '1 1/8 inch':
                        res = (float(i.text()) * float(k.currentText())) * 3.676
                        total.append(res)
                    elif j.currentText() == '1 1/4 inch':
                        res = (float(i.text()) * float(k.currentText())) * 4.17
                        total.append(res)
                    elif j.currentText() == '1 1/2 inch':
                        res = (float(i.text()) * float(k.currentText())) * 6.25
                        total.append(res)
                    elif j.currentText() == '----':
                        res = (float(i.text()) * float(k.currentText())) * 0
                        total.append(res)

            output = round((sum(total)/1000), 1)

            if self.lb_btn.isChecked():
                if self.buy_btn.isChecked():
                    output = output*(1-(0.128*(141.5/((float((self.api_btn.text())))+131.5))))
                    output = round(output,1)
                else:
                    output = output
                self.lcd.display(output)
                self.unit_lbl.setText('klbs')

            elif self.ton_btn.isChecked():
                if self.buy_btn.isChecked():
                    output = output * (1 - (0.128 * ((141.5) / ((float((self.api_btn.text()))) + 131.5))))
                else:
                    output = output
                self.lcd.display(round((output*0.45359), 1))
                self.unit_lbl.setText('Tons')

        except:
            QMessageBox.information(None, 'Error', 'Letters are not allowed \nPlease fill all cells with numbers')


my_app = QApplication([])
my_app_window = Calc()
my_app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
my_app.exec_()
