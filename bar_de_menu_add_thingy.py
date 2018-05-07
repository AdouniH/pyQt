import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(800,50,500,300)
        self.setWindowTitle("Houssem ADOUNI")
        self.setWindowIcon(QtGui.QIcon('ENSG.png'))

        """"
        ADD Thingy to menu bar
        """"
        extractAction = QtGui.QAction("&do something", self)
        extractAction.setShortcut("CTRL+Q")
        extractAction.setStatusTip('Leave the app')
        extractAction.triggered.connect(self.close_application)


        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

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
