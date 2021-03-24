
from PySide2.QtWidgets import QMessageBox

from PySide2.QtSql import QSqlDatabase, QSqlQuery

def _createHazListTable():
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
         """
        CREATE TABLE IF NOT EXISTS Hazards (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            NAME TEXT NOT NULL,
            Corrosive INT,
            Flammable INT,
            Hazardous INT,
            Respiratory INT,
            Environment INT,
            Toxic INT,
            HHM INT

        )
        """
    )
def createConnection(databaseName):

    """Create and open a database connection."""

    connection = QSqlDatabase.addDatabase("QSQLITE")

    connection.setDatabaseName(databaseName)


    if not connection.open():

        QMessageBox.warning(

            None,

            "RP Contact",

            f"Database Error: {connection.lastError().text()}",

        )

        return False


    return True
