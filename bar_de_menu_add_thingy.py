import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(800,50,500,300)
        self.setWindowTitle("Houssem ADOUNI")
        self.setWindowIcon(QtGui.QIcon('ENSG.png'))

        """
        ADD Thingy to menu bar
        """
        extractAction = QtGui.QAction("&do something", self)
        extractAction.setShortcut("CTRL+Q")
        extractAction.setStatusTip('Leave the app')
        extractAction.triggered.connect(self.close_application)

        extractAction1 = QtGui.QAction("&do something", self)
        extractAction1.setShortcut("CTRL+Q")
        extractAction1.setStatusTip('Leave the app')
        extractAction1.triggered.connect(self.close_application)

        extractAction2 = QtGui.QAction("&do one other thing", self)
        extractAction2.setShortcut("CTRL+Q")
        extractAction2.setStatusTip('Leave the app')
        extractAction2.triggered.connect(self.close_application)

        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&Menu1')
        fileMenu.addAction(extractAction)

        fileMenu1 = mainMenu.addMenu('&Menu2')
        fileMenu1.addAction(extractAction1)
        fileMenu1.addAction(extractAction2)

        """
        finish of the thingy
        """


        self.home()

    def home(self):
        btn=QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(100,100)
        self.show()

    def close_application(self):
        print "custom thingy"
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
