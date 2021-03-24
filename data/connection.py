from PySide2 import QtSql, QtGui
import sqlite3
import re
from PySide2.QtCore import QFile

def createConnection():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("LabelBase.db")
    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                QtGui.qApp.tr("Unable to establish a database connection.\n"
                              "This example needs SQLite support. Please read "
                              "the Qt SQL driver documentation for information "
                              "how to build it.\n\nClick Cancel to exit."),
                QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)
        return False

    return True
def sqlite3con():
    try:
        con = sqlite3.connect("LabelBase.db")
    except Exception as e:
        print(e)
        sqlfile = open("exported2.sql")
        sqlfilestr = sqlfile.read()
        sqlite3.Cursor.executescript(sqlfilestr)
        con = sqlite3.connect("LabelBase.db")


    return con
def createCorrosiveList(con):
    cur = con.cursor()
    chemicals = []
    cur.execute("SELECT Chemical FROM ChemicalHazards WHERE Corrosive='TRUE'")
    rows = cur.fetchall()
    for row in rows:
        a = row
        (chemical, ) =a
        chemicals.append(chemical)
    return chemicals
def createFlammableList(con):
    cur = con.cursor()
    chemicals = []
    cur.execute("SELECT Chemical FROM ChemicalHazards WHERE Flammable='TRUE'")
    rows = cur.fetchall()
    for row in rows:
        a = row
        (chemical, ) = a
        chemicals.append(chemical)
    return chemicals    
def createHazardousList(con):
    cur = con.cursor()
    chemicals = []
    cur.execute("SELECT Chemical FROM ChemicalHazards WHERE Hazardous='TRUE'")
    rows = cur.fetchall()
    for row in rows:
        a = row
        (chemical, ) = a
        chemicals.append(chemical)
    return chemicals
def createEnvironmentList(con):
    cur = con.cursor()
    chemicals = []
    cur.execute("SELECT Chemical FROM ChemicalHazards WHERE Environment='TRUE'")
    rows = cur.fetchall()
    for row in rows:
        a = row
        (chemical, ) = a
        chemicals.append(chemical)
    return chemicals
def createRespiratoryList(con):
    cur = con.cursor()
    chemicals = []
    cur.execute("SELECT Chemical FROM ChemicalHazards WHERE Respiratory='TRUE'")
    rows = cur.fetchall()
    for row in rows:
        a = row
        (chemical, ) = a
        chemicals.append(chemical)
    return chemicals
def createToxicList(con):
    cur = con.cursor()
    chemicals = []
    cur.execute("SELECT Chemical FROM ChemicalHazards WHERE Toxic='TRUE'")
    rows = cur.fetchall()
    for row in rows:
        a = row
        (chemical, ) = a
        chemicals.append(chemical)
    return chemicals
def createHHMList(con):
    cur = con.cursor()
    chemicals = []
    cur.execute("SELECT Chemical FROM ChemicalHazards WHERE HHM='TRUE'")
    rows = cur.fetchall()
    for row in rows:
        a = row
        (chemical, ) = a
        chemicals.append(chemical)
    return chemicals
def checkIfResult(con, results):
    cur = con.cursor()
    cur.execute("SELECT OldName, CorrectSpelling From Replacements")
    tabdict = {}
    for (OldName, CorrectSpelling) in cur:
        tabdict[OldName] = CorrectSpelling

    reslist= results.split(", ")
    reslist = [tabdict.get(item, item) for item in reslist]
    
    
    return ", ".join(reslist)
def remove(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    return list
        
        


