import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setGeometry(800,50,500,300)
window.setWindowTitle("Houssem ADOUNI")
window.show()
sys.exit(app.exec_())