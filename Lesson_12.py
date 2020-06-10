import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton

# создание приложения
app = QApplication(sys.argv)

# создание окна
window = QWidget()

window.setGeometry(100, 100, 300, 300)
window.move(500, 500)
Msg = QLabel('<h1>Hello!</h1>', parent=window)
Msg.move(100,15)

window.move(100, 50)
ok_button = QPushButton('Ok', parent=window)
ok_button.move(100,50)

window.show()
sys.exit(app.exec())

