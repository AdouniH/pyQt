import sys
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(800,50,500,300)
        self.setWindowTitle("Houssem ADOUNI")
        self.setWindowIcon(QtGui.QIcon('ENSG.png'))
        self.show()

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
