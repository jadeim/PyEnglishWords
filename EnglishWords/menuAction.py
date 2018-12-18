from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction,qApp, QMenu,QFileDialog

class M_Action(QWidget):
    def __init__(self):
        super().__init__()


    def menuActionExit(self):
        actExit = qApp.quit
        return actExit

    def pushLoadMenuClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        return fname

if __name__ == '__main__':
    act = M_Action()
    act.menuActionExit()