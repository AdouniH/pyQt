import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(800,50,500,300)
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

        # thingy one
        extractAction = QtGui.QAction(QtGui.QIcon('ENSG.png'), 'hello1', self)
        extractAction.triggered.connect(self.close_application)

        #thingy two
        extractAction1 = QtGui.QAction(QtGui.QIcon('ENSG.png'), 'hello2', self)
        extractAction.triggered.connect(self.close_application)

        #thingy three
        extractAction2 = QtGui.QAction(QtGui.QIcon('ENSG.png'), 'hello3', self)
        extractAction.triggered.connect(self.close_application)

        #add toolbar and put the thingies on it
        self.toolBar = self.addToolBar("extraction")
        self.toolBar.addAction(extractAction)
        self.toolBar.addAction(extractAction1)

        #ajout d'un autre toolbar
        self.toolBar = self.addToolBar("extraction2")
        self.toolBar.addAction(extractAction)



        self.show()

    def close_application(self):
        print "custom thingy"
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
