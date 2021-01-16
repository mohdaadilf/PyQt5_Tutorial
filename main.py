from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "First Program"
        self.x = 510
        self.y = 170
        self.width = 300
        self.height = 400
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("hdds.ico"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
