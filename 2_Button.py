from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.title = "Button"
        self.x = 510
        self.y = 170
        self.width = 300
        self.height = 400
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("hdds.ico"))
        self.UiComponents()
        self.statusBar().showMessage("Status Bar")
        self.show()

    def UiComponents(self):
        button = QPushButton('Click here', self)
        button.setToolTip('This is an example button')
        button.move(100, 150)
        button.setIcon(QtGui.QIcon("hdds.ico"))
        button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        self.statusBar().showMessage("Button Clicked")

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
