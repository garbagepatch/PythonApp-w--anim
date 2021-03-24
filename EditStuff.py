from PySide2.QtWidgets import QApplication, QWidget, QTableView, QAbstractItemView, QVBoxLayout
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtSql import *
from PySide2.QtWidgets import QWidget
from HazardTable import Ui_HazardTable
from PySide2.QtWidgets import QDialog
from PySide2 import QtGui, QtCore

class HazardModel(QSqlTableModel):
    def __init__(self, tableName, parent=None):
        super(HazardModel,self).__init__(parent)
        self.setTable(tableName)
        self.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.select()
        self.setHeaderData(0, Qt.Horizontal, "id")
        self.setHeaderData(1, Qt.Horizontal, "Chemical")
        self.setHeaderData(2, Qt.Horizontal,"Corrosive")
        self.setHeaderData(3, Qt.Horizontal, "Flammable")
        self.setHeaderData(4, Qt.Horizontal, "Hazardous")
        self.setHeaderData(5, Qt.Horizontal, "Environment")
        self.setHeaderData(6, Qt.Horizontal, "Respiratory")
        self.setHeaderData(7, Qt.Horizontal, "Toxic")
        self.setHeaderData(8, Qt.Horizontal, "HHM")
class ReplacementModel(QSqlTableModel):
    def __init__(self, myName, parent=None):
        super(ReplacementModel,self).__init__(parent)
        
        self.setTable(myName)
        self.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.select()
        self.setHeaderData(0, Qt.Horizontal, "id")
        self.setHeaderData(1, Qt.Horizontal, "OldName")
        self.setHeaderData(2, Qt.Horizontal, "CorrectSpelling" )
class EditStuff(QDialog, Ui_HazardTable):
    def __init__(self,  parent= None):
        super(EditStuff, self).__init__(parent)
        self.setupUi(self)
        self.hazTableName="ChemicalHazards"
        self.replacementTableName="Replacements"
        self.hazModel = HazardModel(self.hazTableName)
        self.tableView.setModel(self.hazModel)
        self.replacementModel = ReplacementModel(self.replacementTableName)
        self.replacementTable.setModel(self.replacementModel)
        self.delRow = -1
        self.tableView.clicked.connect(self.findRow)
        self.addHazard.clicked.connect(self.AddHazard)
        self.deleteHazardButton.clicked.connect(self.deleteHazard)
        self.replacementTable.clicked.connect(self.findRow)
        self.deleteReplacementButton.clicked.connect(self.deleteReplacement)
        self.addReplacementButton.clicked.connect(self.AddReplacement)
    def findRow(self, i):
        self.delRow = i.row()
    def AddHazard(self):
       
        self.hazModel.insertRows(self.hazModel.rowCount(), 1)
        
    def AddReplacement(self):
        self.replacementModel.insertRows(self.replacementModel.rowCount(),1)
    def deleteReplacement(self):
        self.replacementModel.removeRow(self.replacementTable.currentIndex().row())
    def deleteHazard(self):
        self.hazModel.removeRow(self.tableView.currentIndex().row())









