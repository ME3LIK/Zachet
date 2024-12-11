from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QInputDialog, QMessageBox

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('untitled.ui', self)

        self.pushButton_tab1.clicked.connect(self.show_message)
        self.pushButton_tab2.clicked.connect(self.sum_checkboxes)
        self.pushButton_tab3_1.clicked.connect(self.input_number_1)
        self.pushButton_tab3_2.clicked.connect(self.input_number_2)
        self.pushButton_tab3_calculate.clicked.connect(self.calculate)
        self.comboBox_countries.currentIndexChanged.connect(self.show_flag)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

    def show_message(self):
        text = self.lineEdit_tab1.text()
        if text.isdigit():
            self.label_tab1_result.setText(f"Вы ввели: {text}")
        else:
            self.label_tab1_result.setText("Введите целое число!")

    def sum_checkboxes(self):
        total = 0
        if self.checkBox_1.isChecked():
            total += 1
        if self.checkBox_2.isChecked():
            total += 10
        if self.checkBox_3.isChecked():
            total += 100
        self.label_tab2_result.setText(f"Сумма: {total}")

    def input_number_1(self):
        text, ok = QInputDialog.getDouble(self, "Ввод 1", "Введите число:", 0, -99999, 99999, 2)
        if ok:
            self.number1 = text
            self.label_input1.setText(f"Введено 1: {self.number1}")

    def input_number_2(self):
        text, ok = QInputDialog.getDouble(self, "Ввод 2", "Введите число:", 0, -99999, 99999, 2)
        if ok:
            self.number2 = text
            self.label_input2.setText(f"Введено 2: {self.number2}")

    def calculate(self):
        if hasattr(self, 'number1') and hasattr(self, 'number2'):
            a = self.number1
            b = self.number2

            if self.radioButton_add.isChecked():
                result = a + b
            elif self.radioButton_subtract.isChecked():
                result = a - b
            elif self.radioButton_multiply.isChecked():
                result = a * b
            elif self.radioButton_divide.isChecked():
                if b != 0:
                    result = a / b
                else:
                    result = "Деление на ноль!"
            else:
                result = "Выберите операцию!"

            self.label_tab3_result.setText(str(result))

    def show_flag(self):
        country = self.comboBox_countries.currentText()
        if country == "Россия":
            self.label_country_flag.setPixmap(QtGui.QPixmap("flag_russia.png"))
        elif country == "Англия":
            self.label_country_flag.setPixmap(QtGui.QPixmap("flag_uk.png"))
        elif country == "США":
            self.label_country_flag.setPixmap(QtGui.QPixmap("flag_usa.png"))
app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()