import sys
import json
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtCore import Qt

design_path = 'mainwindow.ui'
Ui_Mainwindow, QtBaseClass = uic.loadUiType(design_path)
tick = QtGui.QImage('tick.png')


class TodoModel(QtCore.QAbstractListModel):

    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text

        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)

class MainWindow(QtWidgets.QMainWindow, Ui_Mainwindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Mainwindow.__init__(self)
        self.ui = Ui_Mainwindow()
        self.ui.setupUi(self)
        self.model = TodoModel()
        self.ui.todoView.setModel(self.model)
        self.ui.addButton.pressed.connect(self.add)
        self.ui.deleteButton.pressed.connect(self.delete)

    def add(self):
        text = self.ui.todoEdit.text()
        if text:
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            self.ui.todoEdit.setText("")

    def delete(self):
        indexes = self.ui.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.ui.todoView.clearSelection()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())