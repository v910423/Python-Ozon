import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFormLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Форма')
layout = QFormLayout()
layout.addRow('Имя: ', QLineEdit())
layout.addRow('Фамилия: ', QLineEdit())
layout.addRow('Возраст: ', QLineEdit())
layout.addRow('Телефон: ', QLineEdit())
layout.addRow(QPushButton('Ok'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())