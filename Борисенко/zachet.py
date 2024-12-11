from PyQt5 import QtWidgets
import form

class Mywindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = form.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.odin)
        self.ui.pushButton_4.clicked.connect(self.tri)
        self.ui.pushButton_5.clicked.connect(self.vihod)

    def odin(self):
        a = self.ui.lineEdit.text()
        self.ui.label_5.setText(a)

    def dva(self):
        if self.ui.checkBox.isChecked():
            self.ui.label_2.setText("5")
        if self.ui.checkBox_2.isChecked():
            self.ui.label_2.setText("15")
        if self.ui.checkBox_3.isChecked():
            self.ui.label_2.setText("50")
        if self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked():
            self.ui.label_2.setText("20")
        if self.ui.checkBox.isChecked() and self.ui.checkBox_3.isChecked():
            self.ui.label_2.setText("55")
        if self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked():
            self.ui.label_2.setText("65")

    def tri(self):
        a = self.ui.lineEdit_2.text()
        b = self.ui.lineEdit_3.text()
        if self.ui.radioButton.isChecked():
            self.ui.label_3.setText(a+b)
        if self.ui.radioButton_2.isChecked():
            self.ui.label_3.setText(a-b)
        if self.ui.radioButton_3.isChecked():
            self.ui.label_3.setText(a*b)
        if self.ui.radioButton_4.isChecked():
            self.ui.label_3.setText(a/b)
    def vihod(self):


