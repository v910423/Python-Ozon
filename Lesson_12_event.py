import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel

def greeting():
    if msg.text():
        msg.setText("")
    else:
        msg.setText('Hi.')

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Less12')
layout = QVBoxLayout()

btn = QPushButton('hello!!!')
btn.clicked.connect(greeting)

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())