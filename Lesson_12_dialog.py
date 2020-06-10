import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QInputDialog

class example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    data = ''

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.clicked.connect(self.showDialog)
        self.le = QLabel('', self)
        self.le.move(5, 50)
        self.le.setFixedHeight(300)
        self.le.setFixedWidth(200)
        self.setGeometry(500, 500, 350, 250)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input', 'Name: ')

        if ok:
            self.data += str(text) + '\n'
            self.le.setText(str(self.data))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())