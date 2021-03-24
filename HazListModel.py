from PySide2.QtCore import *
from PySide2.QtSql import  QSqlTableModel

class HazListModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("Hazards")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers=("ID","Name", "Corrosive", "Flammable", "Hazardous", "Respiratory", "Environment", "Toxic", "HHM" )
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel