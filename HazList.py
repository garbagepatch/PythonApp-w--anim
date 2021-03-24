
from PySide2.QtSql import *
from PySide2.QtWidgets import (QAbstractItemView, QHBoxLayout, QMainWindow, QPushButton, QTableView, QVBoxLayout, QWidget)
from HazListModel import HazListModel
class Hazlist(QMainWindow):
    def __init__(self  ):
        self.hazListModel = HazListModel()
        self.setupUi()
    def setupUi(self):
        self.table = QTableView()
        self.table.setModel(self.hazListModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        self.addButton = QPushButton("Add ...")
        self.deleteButton = QPushButton("Delete ...")
        self.clearButton = QPushButton("Clear ...")
        layout =QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearButton)
        self.Hazlist.addWidget(self.table)
        self.layout.addLayout(layout)