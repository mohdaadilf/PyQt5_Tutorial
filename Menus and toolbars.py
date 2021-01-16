import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QAction, QMenu, QTextEdit
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Status bar')
        self.show()

        self.statusbar = self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')  # creating menu

        exitAct = QAction(QIcon('hdds.ico'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        impmenu = QMenu('Import', self)  # sub menu
        impAct = QAction('Import mail', self)
        impmenu.addAction(impAct)

        viewStatAct = QAction('View Statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        fileMenu.addAction(exitAct)
        fileMenu.addAction(viewStatAct)
        fileMenu.addMenu(impmenu)

        self.toolbar = self.addToolBar('')
        self.toolbar.addAction(exitAct)
        self.toolbar.addAction(viewStatAct)

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
            self.statusbar.showMessage("On")
        else:
            self.statusbar.hide()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:

            event.accept()
        else:
            event.ignore()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            self.close()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
