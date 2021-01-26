import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QMainWindow,
                             QVBoxLayout, QApplication, QLabel, QGridLayout, QPushButton,QStatusBar)


class Communicate(QObject):

    closeApp = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def LCDSlider(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        wigd = QWidget()
        grid = QGridLayout()
        x = 0
        y = 0
        self.text = f'x: {x},  y: {y}'
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        wigd.setMouseTracking(True)

        btn1 = QPushButton("Button 1", self)
        grid.addWidget(btn1, 1, 0)

        btn2 = QPushButton("Button 2", self)
        grid.addWidget(btn2, 2, 0)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        wigd.setLayout(grid)
        self.statusBar
        self.setCentralWidget(wigd)

        self.setWindowTitle('Signal and slot')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = f'x: {x},  y: {y}'
        self.label.setText(text)

        self.c.closeApp.emit()
        
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
