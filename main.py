#PyQt5
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QPushButton, QCheckBox,QRadioButton,QButtonGroup,
                             QLineEdit)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click me!", self)
        self.setWindowTitle("First GUI")
        self.setGeometry(700, 400, 500, 500)
        self.setWindowIcon(QIcon("image.jpg"))
        self.label = QLabel("Hello", self)
        self.label1 = QLabel(self)
        self.checkbox = QCheckBox("Do you like anime?", self)
        self.radio1 = QRadioButton("Like", self)
        self.radio2 = QRadioButton("Super-Like", self)
        self.radio3 = QRadioButton("Super-Duper-Like", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.line_edit = QLineEdit(self)
        self.button1 = QPushButton("Submit", self)
        self.initUI()

        #add self. to these below:
        #label.setAlignment(Qt.AlignTop)  # Veritcally TOP
        #label.setAlignment(Qt.AlignBottom)  # Veritcally BOTTOM
        #label.setAlignment(Qt.AlignVCenter)  # V CENTER

        #label.setAlignment(Qt.AlignRight)  # H RIGHT
        #label.setAlignment(Qt.AlignHCenter)  # H CENTERR
        #label.setAlignment(Qt.AlignLeft)  # HORIZONTALLY LEFT

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER & CENTER
        #self.label.setAlignment(Qt.AlignCenter) # CENTER & CENTER
        #self.label1 = QLabel(self)
        #label1.setGeometry(0,0,100,100)
        #pixmap = QPixmap("image.jpg")
        #label1.setPixmap(pixmap)
        #label1.setScaledContents(True)
        #self.label1.setGeometry((self.width() - self.label1.width()) // 2,
        #                        (self.height() - self.label1.height()) // 2,
        #                        self.label1.width(),
        #                        self.label1.height())

    def initUI(self):

        self.checkbox.setGeometry(10, 190, 500, 90)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

        self.radio1.setGeometry(10, 240, 400, 70)
        self.radio2.setGeometry(10, 280, 400, 70)
        self.radio3.setGeometry(10, 320, 400, 70)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 25px;"
                           "font-family: Arial;"
        #                   "padding: 20px;"
                           "}")
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group2.addButton(self.radio3)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)

        self.button.setGeometry(150,100,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setFont(QFont("Arial", 40))
        self.label.setGeometry(0, 0, 500, 100)
        self.label.setStyleSheet("color: #000000;"
                                 "background-color: #612aa3;"
                                 "font-weight: bold;"
                                 "font-style: italic;"
                                 "text-decoration: underline;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label1.setGeometry(0,0,100,100)
        pixmap = QPixmap("image.jpg")
        self.label1.setPixmap(pixmap)
        self.label1.setScaledContents(True)
        self.label1.setGeometry(0,
                            0,
                            self.label1.width(),
                            self.label1.height())
        self.line_edit.setGeometry(10,400,300,40)
        self.button1.setGeometry(310,400,120,40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "fon-family: Arial;"
                                     )
        self.button1.setStyleSheet("font-size: 20px;"
                                     "fon-family: Arial;"
                                     )
        self.line_edit.setPlaceholderText("Enter your anime")
        self.button1.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Your anime is {text}")
        self.button1.setText("Submitted")
        self.button1.setDisabled(True)
    def on_click(self):
        self.label.setText("Goodbye")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        #central_widget = QWidget()
        #self.setCentralWidget(central_widget)

        #label1 = QLabel("#1", self)
        #label2 = QLabel("#2", self)
        #label3 = QLabel("#3", self)
        #label4 = QLabel("#4", self)
        #label5 = QLabel("#5", self)

        #label1.setStyleSheet("background-color: red;")
        #label2.setStyleSheet("background-color: yellow;")
        #label3.setStyleSheet("background-color: green;")
        #label4.setStyleSheet("background-color: purple;")
        #label5.setStyleSheet("background-color: blue;")

        #grid = QGridLayout()
        #grid.addWidget(label1, 0, 0)
        #grid.addWidget(label2, 0, 1)
        #grid.addWidget(label3, 1, 0)
        #grid.addWidget(label4, 1, 1)
        #grid.addWidget(label5, 1, 2)

        #central_widget.setLayout(grid)
    def checkbox_changed(self, state):
        #print(state)
        if state == Qt.Checked:
            print("You like anime")
        else:
            print("You DO NOT like anime")

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is given!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
