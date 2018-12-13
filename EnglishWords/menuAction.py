from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction,qApp, QMenu

class M_Action:
    def __init__(self):
        pass

    def menuActionExit(self):
        actExit = qApp.quit
        return actExit

if __name__ == '__main__':
    act = M_Action()
    act.menuActionExit()