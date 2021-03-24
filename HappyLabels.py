from UserInputWindow import Ui_MainWindow
from Label import Label

from PySide2 import QtWidgets, QtCore, QtGui
import pyqtgraph.opengl as gl
from PySide2.QtGui import QIcon, QImage, QPixmap
from PySide2.QtWidgets import  QMainWindow, QAction
from EditStuff import EditStuff
from datetime import date
import numpy as np
from opensimplex import OpenSimplex
import sys
from data.connection import createConnection
class HappyLabels(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(HappyLabels, self).__init__()
        self.setupUi(self)
        sys.stdout = self
        self.w = gl.GLViewWidget()
        self.w.setGeometry(0, 110, 1920, 1080 )
        self.w.show()
        self.nsteps = 1
        self.ypoints = range(-20, 22, self.nsteps)
        self.xpoints = range(-20, 22, self.nsteps)
        self.nfaces = len(self.ypoints)
        self.offset = 0
        self.tmp = OpenSimplex()
        verts = np.array([
            [
                x, y, 1.5 * self.tmp.noise2d(x=n / 5, y=m / 5)
            ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)
        ], dtype=np.float32)
        faces = []
        colors = []
        for m in range(self.nfaces - 1):
            yoff = m * self.nfaces
            for n in range(self.nfaces - 1):
                faces.append([n + yoff, yoff + n + self.nfaces, yoff + n + self.nfaces + 1])
                faces.append([n + yoff, yoff + n + 1, yoff + n + self.nfaces + 1])
                colors.append([0, 0, 0, 0])
                colors.append([0, 0, 0, 0])

        faces = np.array(faces)
        colors = np.array(colors)

        # create the mesh item
        self.m1 = gl.GLMeshItem(
            vertexes=verts,
            faces=faces, faceColors=colors,
            smooth=False, drawEdges=True,
        )
        self.m1.setGLOptions('additive')
        self.w.addItem(self.m1)

        self.pushButton.clicked.connect(self.OpenLabels)
        self.comboBox.currentTextChanged.connect(self.SetLabels)
        self.setWindowTitle("Sup")
        self.pH = 0
        self.isMedia = False
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
        self.editthing = None
        self.createMenu()
    def start(self):
        """
        get the graphics window open and setup
        """
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def update(self):
        """
        update the mesh and shift the noise each time
        """
        verts = np.array([
            [
                x, y, 2.5 * self.tmp.noise2d(x=n / 5 + self.offset, y=m / 5 + self.offset)
            ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)
        ], dtype=np.float32)

        faces = []
        colors = []
        for m in range(self.nfaces - 1):
            yoff = m * self.nfaces
            for n in range(self.nfaces - 1):
                faces.append([n + yoff, yoff + n + self.nfaces, yoff + n + self.nfaces + 1])
                faces.append([n + yoff, yoff + n + 1, yoff + n + self.nfaces + 1])
                colors.append([n / self.nfaces, 1 - n / self.nfaces, m / self.nfaces, 0.7])
                colors.append([n / self.nfaces, 1 - n / self.nfaces, m / self.nfaces, 0.8])

        faces = np.array(faces, dtype=np.uint32)
        colors = np.array(colors, dtype=np.float32)

        self.m1.setMeshData(
            vertexes=verts, faces=faces, faceColors=colors
        )
        self.offset -= 0.18
    def animation(self):
        """
        calls the update method to run in a loop
        """
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(10)
        self.start()
        self.update()
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
        editAction = QAction(QIcon('save.png'), "edit", self)
        editAction.setShortcut('Ctrl+R')
 
 
 
        exitAction.triggered.connect(self.exit_app)
 

 

        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        editAction.triggered.connect(self.editStuff)
        fileMenu.addAction(exitAction)
        editMenu.addAction(editAction)
 
    def exit_app(self):
        self.close()
    def editStuff(self):
        try:
            self.editthings = EditStuff()
            self.editthings.show()
        except Exception as e:
            print(e)
    def SetLabels(self):
        if(self.comboBox.currentText() == "Media"):
            self.conductivityLabel.setText("pCO2")
            self.conductivityTemperatureLabel.setText("Osmolality")
            self.isMedia = True
            
        if(self.comboBox.currentText() == "Buffers"):
            self.conductivityLabel.setText("Conductivity")
            self.conductivityTemperatureLabel.setText("Conductivity Temp")
            self.isMedia = False
    def OpenLabels(self):
        try: 
            self.listInfo = [self.batchTitleLineEdit.text(),self.emailLineEdit.text(), self.lotNumberLineEdit.text(),  self.deliveryZoneComboBox.currentText(), self.expirationDateDateTimeEdit.date().toString("yyyy-MM-dd"), self.pHLineEdit.text(), self.pHTemperatureLineEdit.text(), self.conductivityLineEdit.text(), self.conductivityTemperatureLineEdit.text() ]    
            self.label = Label(self.listInfo, self.textEdit.toPlainText(), self.isMedia )
            self.label.show()
            
        except Exception as e: 
            print(e)
        


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createConnection()
    app.setStyle('Fusion')
    main = HappyLabels()

    main.show()
    main.animation()
    sys.exit(app.exec_())
