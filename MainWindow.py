from UserInputWindow import Ui_MainWindow
from Label import Label
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QMainWindow, QAction
from PySide2.QtUiTools import QUiLoader
from datetime import date
import sys
from database import createConnection
from HazList import Hazlist

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)  
     
        sys.stdout = self
        self.pushButton.clicked.connect(self.OpenLabels)
        self.setWindowTitle("Sup")
        self.pH = 0
        self.w = self.openGLWidget()
        self.w.setGeometry(0,100,1920,1080)
        self.cond = 0
        self.batchTitle = "Batch"
        self.deliveryZoneComboBox.addItems(["1-B-32", "2-G-12", "3-B-11", "3-J-11", "4th Floor Rt", "4th Floor Cold", "4th Floor H-Room", "5th Floor Rt", "5th Floor Cold", "5th Floor H-Room", "6th Floor RT", "6th Floor Cold", "6th Floor BST", "6th Floor H-Room", "SUL"])
        self.pHtemp = 27
        self.contemp = 25
        self.email = "email@email.com"
        self.lotnumber = "A20111111"
        self.date = date.today()
        self.expdate = date.today()
        self.listInfo = []
        self.label = None
        self.createMenu()
        self.Hazlist = None

    def createMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        viewMenu = mainMenu.addMenu('View')
        editMenu = mainMenu.addMenu('Edit')
        fontMenu = mainMenu.addMenu('Font')
        helpMenu = mainMenu.addMenu('Help')
 
 
        openAction = QAction(QIcon('open.png'), "Open", self)
        openAction.setShortcut('Ctrl+O')
 
 
        saveAction = QAction(QIcon('save.png'), "Save", self)
        saveAction.setShortcut('Ctrl+S')
 
        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut('Ctrl+X')

        editHazlistAction = QAction(QIcon('open.png'), "Edit Hazards", self)
        editHazlistAction.setShortcut('Ctrl+I')
 
 
 
        exitAction.triggered.connect(self.exit_app)
        editHazlistAction.triggered.connect(self.edit_hazlist)

        editMenu.addAction(editHazlistAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)
    def edit_hazlist(self):
        if self.Hazlist is None:
            self.Hazlist = Hazlist()
            self.Hazlist.show()
    def exit_app(self):
        self.close()

    def OpenLabels(self):
        try: 
            self.listInfo = [self.batchTitleLineEdit.text(),self.emailLineEdit.text(), self.lotNumberLineEdit.text(),  self.deliveryZoneComboBox.currentText(), self.expirationDateDateTimeEdit.date().toString("yyyy-MM-dd"), self.pHLineEdit.text(), self.pHTemperatureLineEdit.text(), self.conductivityLineEdit.text(), self.conductivityTemperatureLineEdit.text() ]    
            self.label = Label(self.listInfo )
            self.label.show()
            
        except Exception as e: 
            print(e)
        


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    if not createConnection("database.db"):
        sys.exit(1)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
