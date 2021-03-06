import sys

# import Logo_rc
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiSubWindow

from HomeWindow import Ui_HomeWindow
from MainWindow import Ui_MainWindow
from ValveSim import Ui_ValveSim


class HomeWindow(QMainWindow, Ui_HomeWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)


class ValveSim(QMainWindow, Ui_ValveSim):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)


class Win1(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.vs = ValveSim()
        self.hw = HomeWindow()
        self.CreateValveSimulator()
        self.CreateWindow()

    def CreateValveSimulator(self):
        subwindow = QMdiSubWindow()
        subwindow.setWidget(self.vs)
        self.mdiArea.addSubWindow(subwindow)
        subwindow.setFixedSize(500, 500)
        # self.subwindow.close()

    def CreateWindow(self):
        
        self.hw.pushButton.clicked.connect(self.vs.showNormal)
        subwindow = QMdiSubWindow()
        subwindow.setWindowFlags(Qt.CustomizeWindowHint | Qt.Tool)
        subwindow.setWidget(self.hw)
        self.mdiArea.addSubWindow(subwindow)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win1()
    win.show()
    sys.exit(app.exec_())
