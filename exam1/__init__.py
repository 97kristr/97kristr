
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import Model



class Exam1(QMainWindow):
  
  def __init__(self, parent=None):
    super(Exam1, self).__init__()
    
    self.setWindowTitle("Exam template")
    self.initUI()

  def initUI(self):
    """initierar alla komponenter"""  
    
  def run(self):
    self.show() #ser till att komponenterna kan ses.
    sys.exit(app.exec())
  
app = QApplication(sys.argv) #skickar kommando till windows
Exam1().run() #kör applicationen
  
    
    
    
