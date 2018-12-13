import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction,qApp, QMenu
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui,QtCore
from menuAction import M_Action

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyEnglishWords Game"
        self.left = 100
        self.top = 100
        self.width = 1280
        self.height = 786
        self.initUI()

    def initUI(self):
        #self.statusBar()
        self.showWindow()
        self.createrToolbar()

    def createMenu(self):
        """
        ===============================================================================
          Create main menu
        ===============================================================================
        """
        menubar = self.menuBar()
        self.fileMenu = menubar.addMenu('&File')
        self.editMenu = menubar.addMenu('&Edit')
        self.gameMenu = menubar.addMenu('&Game')
        self.helpMenu = menubar.addMenu('&Help')
        self.addMenuToFile()

        """
        ===============================================================================
         adding submenu to File menu   
        ===============================================================================
        """

    def createrToolbar(self):
        SM_exit = self.subMenuExit()
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(SM_exit)

    def addMenuToFile(self):
        subNew = self.subMenuNew()
        subSave = self.subMenuSave()
        subSaveAs = self.subMenuSaveAs()
        subLoad = self.subMenuLoad()
        subPrint = self.subMenuPrint()
        subExit = self.subMenuExit()
        self.fileMenu.addAction(subNew)
        self.fileMenu.addAction(subSave)
        self.fileMenu.addAction(subSaveAs)
        self.fileMenu.addAction(subLoad)
        self.fileMenu.addAction(subPrint)
        self.fileMenu.addAction(subExit)

        subUndo = self.subMenuUndo()
        subRedo = self.subMenuRedo()
        subCut = self.subMenuCut()
        subCopy = self.subMenuCopy()
        subPaste = self.subMenuPaste()
        self.editMenu.addAction(subUndo)
        self.editMenu.addAction(subRedo)
        self.editMenu.addAction(subCut)
        self.editMenu.addAction(subCopy)
        self.editMenu.addAction(subPaste)

        subWord = self.subMenuWord()
        subSentence = self.subMenuSentence()
        self.gameMenu.addAction(subWord)
        self.gameMenu.addAction(subSentence)

        subHelp = self.subMenuHelp()
        subAbout = self.subMenuAbout()
        self.helpMenu.addAction(subHelp)
        self.helpMenu.addAction(subAbout)



    def subMenuNew(self):
        """
        ===============================================================================
         sub-menu creation : New menu
        ===============================================================================
        """
        newFile = QAction('&New', self)
        newFile.setShortcut('Ctrl+N')
        newFile.setStatusTip('New File')
        return newFile

    def subMenuSave(self):
        """
        ===============================================================================
          Save menu
        ===============================================================================
        """
        saveFile = QAction("&Save", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)
        return saveFile

    def subMenuLoad(self):
        """
        ===============================================================================
         Load menu
        ===============================================================================
        """
        loadFile = QAction('&Load', self)
        loadFile.setShortcut('Ctrl+L')
        loadFile.setStatusTip('Load file')
        return loadFile

    def subMenuSaveAs(self):
        """
        ===============================================================================
         Save as menu
        ===============================================================================
        """
        saveAsFile = QAction('&Save As', self)
        saveAsFile.setShortcut('Ctrl+shift+S')
        saveAsFile.setStatusTip('Save As file')
        return saveAsFile

    def subMenuPrint(self):
        """
        ===============================================================================
         Print menu
        ===============================================================================
        """
        printFile = QAction('&Print', self)
        printFile.setShortcut('Ctrl+P')
        printFile.setStatusTip('Print file')
        return printFile

    def subMenuExit(self):
        """
        =============================================================================
         exit menu
        =============================================================================
        """
        exitMenu = QAction(QIcon('resource\Image\Exit.png'), '&Exit', self)
        exitMenu.setShortcut('Ctrl+Q')
        exitMenu.setStatusTip('Exit application')
        exitAction = M_Action()
        exitMenu.triggered.connect(exitAction.menuActionExit())

        return exitMenu

    def subMenuUndo(self):
        """
        =============================================================================
         Undo menu
        =============================================================================
        """
        undoMenu = QAction('&Undo',self)
        undoMenu.setShortcut('Ctrl+Z')
        undoMenu.setStatusTip('Undo files')
        return undoMenu

    def subMenuRedo(self):
        """
        =============================================================================
         Redo menu
        =============================================================================
        """
        redoMenu = QAction('&Redo',self)
        redoMenu.setShortcut('Ctrl+Y')
        redoMenu.setStatusTip('Redo files')
        return redoMenu

    def subMenuCut(self):
        """
        =============================================================================
         Cut menu
        =============================================================================
        """
        cutMenu = QAction('&Cut',self)
        cutMenu.setShortcut('Ctrl+X')
        cutMenu.setStatusTip('Cut words')
        return cutMenu

    def subMenuCopy(self):
        """
        =============================================================================
         Copy menu
        =============================================================================
        """
        copyMenu = QAction('&Copy',self)
        copyMenu.setShortcut('Ctrl+C')
        copyMenu.setStatusTip('Copy words')
        return copyMenu

    def subMenuPaste(self):
        """
        =============================================================================
         Paste menu
        =============================================================================
        """
        pasteMenu = QAction('&Paste',self)
        pasteMenu.setShortcut('Ctrl+V')
        pasteMenu.setStatusTip('Paste words')
        return pasteMenu

    def subMenuWord(self):
        """
        =============================================================================
         word typing game menu in game menu
        =============================================================================
        """
        wordMenu = QAction('&Word Typing',self)
        return wordMenu

    def subMenuSentence(self):
        """
        =============================================================================
         sentence typing game menu in game menu
        =============================================================================
        """
        sentenceMenu = QAction('&Sentence Typing',self)
        return sentenceMenu

    def subMenuHelp(self):
        """
        =============================================================================
         'How to do' information for this program in Help menu
        =============================================================================
        """
        helpMenu = QAction('&Help',self)
        helpMenu.setShortcut('F1')
        helpMenu.setStatusTip('Program information')
        return helpMenu

    def subMenuAbout(self):
        """
        =============================================================================
         version information of this program
        =============================================================================
        """
        aboutMenu = QAction('&About',self)
        aboutMenu.setStatusTip('version information')
        return aboutMenu

    def showWindow(self):
        """
        ===============================================================================
         Showing whole menu
        ===============================================================================
        """

        """
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
"""
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon('resource\Image\Window_Icon.png'))
        self.createMenu()
        self.show()


    def file_save(self):
       name = QtGui.QFileDialog.getSaveFileName(self,'Save File')
       file = open(name,'W')
       text = self.textEdit.toPlainText()
       file.write(text)
       file.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showWindow = MainWindow()
    sys.exit(app.exec_())