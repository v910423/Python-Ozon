import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Форма')
layout = QVBoxLayout()

layout.addWidget(QPushButton('verh'))
layout.addWidget(QPushButton('center'))
layout.addWidget(QPushButton('niz'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())