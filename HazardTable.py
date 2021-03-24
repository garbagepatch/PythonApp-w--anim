# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangeStuffDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HazardTable(object):
    def setupUi(self, HazardTable):
        if not HazardTable.objectName():
            HazardTable.setObjectName(u"HazardTable")
        HazardTable.resize(1019, 438)
        self.buttonBox = QDialogButtonBox(HazardTable)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(540, 330, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.tableView = QTableView(HazardTable)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 20, 401, 281))
        self.replacementTable = QTableView(HazardTable)
        self.replacementTable.setObjectName(u"replacementTable")
        self.replacementTable.setGeometry(QRect(475, 21, 411, 281))
        self.replacementTable.setSizeIncrement(QSize(5, 5))
        self.horizontalLayoutWidget = QWidget(HazardTable)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 300, 381, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.deleteHazardButton = QPushButton(self.horizontalLayoutWidget)
        self.deleteHazardButton.setObjectName(u"deleteHazardButton")

        self.horizontalLayout.addWidget(self.deleteHazardButton)

        self.editHazardButton = QPushButton(self.horizontalLayoutWidget)
        self.editHazardButton.setObjectName(u"editHazardButton")

        self.horizontalLayout.addWidget(self.editHazardButton)

        self.addHazard = QPushButton(self.horizontalLayoutWidget)
        self.addHazard.setObjectName(u"addHazard")

        self.horizontalLayout.addWidget(self.addHazard)

        self.horizontalLayoutWidget_2 = QWidget(HazardTable)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(490, 300, 381, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.deleteReplacementButton = QPushButton(self.horizontalLayoutWidget_2)
        self.deleteReplacementButton.setObjectName(u"deleteReplacementButton")

        self.horizontalLayout_2.addWidget(self.deleteReplacementButton)

        self.editReplacementButton = QPushButton(self.horizontalLayoutWidget_2)
        self.editReplacementButton.setObjectName(u"editReplacementButton")

        self.horizontalLayout_2.addWidget(self.editReplacementButton)

        self.addReplacementButton = QPushButton(self.horizontalLayoutWidget_2)
        self.addReplacementButton.setObjectName(u"addReplacementButton")

        self.horizontalLayout_2.addWidget(self.addReplacementButton)


        self.retranslateUi(HazardTable)
        self.buttonBox.accepted.connect(HazardTable.accept)
        self.buttonBox.rejected.connect(HazardTable.reject)

        QMetaObject.connectSlotsByName(HazardTable)
    # setupUi

    def retranslateUi(self, HazardTable):
        HazardTable.setWindowTitle(QCoreApplication.translate("HazardTable", u"Dialog", None))
        self.deleteHazardButton.setText(QCoreApplication.translate("HazardTable", u"Delete", None))
        self.editHazardButton.setText(QCoreApplication.translate("HazardTable", u"Edit", None))
        self.addHazard.setText(QCoreApplication.translate("HazardTable", u"Add", None))
        self.deleteReplacementButton.setText(QCoreApplication.translate("HazardTable", u"Delete", None))
        self.editReplacementButton.setText(QCoreApplication.translate("HazardTable", u"Edit", None))
        self.addReplacementButton.setText(QCoreApplication.translate("HazardTable", u"Add", None))
    # retranslateUi

