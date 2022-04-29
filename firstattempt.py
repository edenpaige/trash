'''
'''
import sys 
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QVBoxLayout ,QMainWindow, QWidget, QLabel, QLineEdit, QApplication
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPixmap

# def zodiac():
#     birthday=int(input("Enter birthdate:"))
#     month =int(birthday[3:5])
#     day = int(birthday[0:2])
#     if month == 4:
#         star_sign = "Aries" if (day < 20) else 'Taurus'
#     print("Your star sign is: ",star_sign)

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zodiac Sign")
        self.setWindowIcon(QtGui.QIcon('zodiac-leo.png'))
        self.setGeometry(450, 300, 250, 130)

        mainLayout = QVBoxLayout()

        self.input1 = QLabel()
        self.input2 = QLabel()
        mainLayout.addWidget(self.input1)
        mainLayout.addWidget(self.input2)
        #I want this to output the starsign... 
        mainLayout.addWidget(QLabel("You are an Aries"))

        self.closeButton = QPushButton("Close")
        self.closeButton.clicked.connect(self.close)
        mainLayout.addWidget(self.closeButton)

        self.setLayout(mainLayout)

    def displayInfo(self):
        self.show()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zodiac")
        self.setWindowIcon(QtGui.QIcon('zodiac-aries.png'))
        self.setFixedWidth(350)

        self.secondWindow = SecondWindow()

        mainLayout = QVBoxLayout()

        self.name = QLineEdit()
        self.age = QLineEdit()
        mainLayout.addWidget(QLabel("Name: "))
        mainLayout.addWidget(self.name)
        mainLayout.addWidget(QLabel("Birthdate: "))
        mainLayout.addWidget(self.age)

        self.confirm = QPushButton("Confirm")
        self.confirm.setStyleSheet('font-size: 16px')
        self.confirm.clicked.connect(self.passingInformation)
        mainLayout.addWidget(self.confirm)

        self.setLayout(mainLayout)

    def passingInformation(self):
        self.secondWindow.input1.setText(self.name.text())
        self.secondWindow.input2.setText(self.age.text())
        self.secondWindow.displayInfo()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())