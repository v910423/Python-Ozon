import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Форма')
layout = QGridLayout()

layout.addWidget(QPushButton('00'), 0, 0)
layout.addWidget(QPushButton('01'), 0, 1)
layout.addWidget(QPushButton('02'), 0, 2)
layout.addWidget(QPushButton('10'), 1, 0)
layout.addWidget(QPushButton('02'), 0, 2)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())