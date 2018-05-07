import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Houssem ADOUNI")
        self.setWindowIcon(QtGui.QIcon('ENSG.png'))


        extractAction = QtGui.QAction("&do something", self)
        extractAction.setShortcut("CTRL+Q")
        extractAction.setStatusTip('Leave the app')
        extractAction.triggered.connect(self.close_application)
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn=QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(0,100)

        extractAction = QtGui.QAction(QtGui.QIcon('ENSG.png'), 'hello', self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("extraction")
        self.toolBar.addAction(extractAction)

        """
        begenning here
        """
        chekbox=QtGui.QCheckBox('Enlarge Window',self)
        chekbox.move(0,25)
        #chekbox.toggle()  #chekbox is on from the beginning
        chekbox.stateChanged.connect(self.enlarge_window)


        self.show()

    def enlarge_window(self,state):
        if state==QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)


    """
    finish
    """
    def close_application(self):
        choice=QtGui.QMessageBox.question(self,'Tile of the window', 'do u really wanna leave ?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice ==QtGui.QMessageBox.Yes:
            print('bye :p') #of course this is in the console
            sys.exit()
        else:
            pass


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
