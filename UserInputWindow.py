# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserInputWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(824, 608)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(179, 240, 227, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(217, 247, 241, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(89, 120, 113, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(119, 160, 151, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 771, 554))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(8)
        self.formLayout_2.setContentsMargins(22, 22, 19, 22)
        self.requestTypeLabel = QLabel(self.horizontalLayoutWidget)
        self.requestTypeLabel.setObjectName(u"requestTypeLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.requestTypeLabel)

        self.comboBox = QComboBox(self.horizontalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox)

        self.batchTitleLabel = QLabel(self.horizontalLayoutWidget)
        self.batchTitleLabel.setObjectName(u"batchTitleLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.batchTitleLabel)

        self.batchTitleLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.batchTitleLineEdit.setObjectName(u"batchTitleLineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.batchTitleLineEdit)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_9)

        self.emailLabel = QLabel(self.horizontalLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.emailLineEdit)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(5, QFormLayout.LabelRole, self.verticalSpacer_8)

        self.lotNumberLabel = QLabel(self.horizontalLayoutWidget)
        self.lotNumberLabel.setObjectName(u"lotNumberLabel")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.lotNumberLabel)

        self.lotNumberLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lotNumberLineEdit.setObjectName(u"lotNumberLineEdit")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.lotNumberLineEdit)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(7, QFormLayout.LabelRole, self.verticalSpacer_7)

        self.deliveryZoneLabel = QLabel(self.horizontalLayoutWidget)
        self.deliveryZoneLabel.setObjectName(u"deliveryZoneLabel")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.deliveryZoneLabel)

        self.deliveryZoneComboBox = QComboBox(self.horizontalLayoutWidget)
        self.deliveryZoneComboBox.setObjectName(u"deliveryZoneComboBox")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.deliveryZoneComboBox)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(9, QFormLayout.LabelRole, self.verticalSpacer_6)

        self.pHLabel = QLabel(self.horizontalLayoutWidget)
        self.pHLabel.setObjectName(u"pHLabel")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.pHLabel)

        self.pHLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.pHLineEdit.setObjectName(u"pHLineEdit")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.pHLineEdit)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(11, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.pHTemperatureLabel = QLabel(self.horizontalLayoutWidget)
        self.pHTemperatureLabel.setObjectName(u"pHTemperatureLabel")

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.pHTemperatureLabel)

        self.pHTemperatureLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.pHTemperatureLineEdit.setObjectName(u"pHTemperatureLineEdit")

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.pHTemperatureLineEdit)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(13, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.conductivityLabel = QLabel(self.horizontalLayoutWidget)
        self.conductivityLabel.setObjectName(u"conductivityLabel")

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.conductivityLabel)

        self.conductivityLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.conductivityLineEdit.setObjectName(u"conductivityLineEdit")

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.conductivityLineEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(15, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.conductivityTemperatureLabel = QLabel(self.horizontalLayoutWidget)
        self.conductivityTemperatureLabel.setObjectName(u"conductivityTemperatureLabel")

        self.formLayout_2.setWidget(16, QFormLayout.LabelRole, self.conductivityTemperatureLabel)

        self.conductivityTemperatureLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.conductivityTemperatureLineEdit.setObjectName(u"conductivityTemperatureLineEdit")

        self.formLayout_2.setWidget(16, QFormLayout.FieldRole, self.conductivityTemperatureLineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(17, QFormLayout.LabelRole, self.verticalSpacer)

        self.expirationDateLabel = QLabel(self.horizontalLayoutWidget)
        self.expirationDateLabel.setObjectName(u"expirationDateLabel")

        self.formLayout_2.setWidget(18, QFormLayout.LabelRole, self.expirationDateLabel)

        self.expirationDateDateTimeEdit = QDateTimeEdit(self.horizontalLayoutWidget)
        self.expirationDateDateTimeEdit.setObjectName(u"expirationDateDateTimeEdit")
        self.expirationDateDateTimeEdit.setDateTime(QDateTime(QDate(2021, 3, 16), QTime(0, 0, 0)))
        self.expirationDateDateTimeEdit.setCalendarPopup(True)
        self.expirationDateDateTimeEdit.setCurrentSectionIndex(0)

        self.formLayout_2.setWidget(18, QFormLayout.FieldRole, self.expirationDateDateTimeEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(19, QFormLayout.LabelRole, self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(206)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(22, 21, 30, 19)
        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.openGLWidget = QOpenGLWidget(self.horizontalLayoutWidget)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.verticalLayout_2.addWidget(self.openGLWidget)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 824, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.requestTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Request Type", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Buffers", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Media", None))

        self.batchTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Batch Title", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lotNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Lot Number", None))
        self.deliveryZoneLabel.setText(QCoreApplication.translate("MainWindow", u"Delivery Zone", None))
        self.pHLabel.setText(QCoreApplication.translate("MainWindow", u"pH", None))
        self.pHTemperatureLabel.setText(QCoreApplication.translate("MainWindow", u"pH temperature", None))
        self.conductivityLabel.setText(QCoreApplication.translate("MainWindow", u"Conductivity", None))
        self.conductivityTemperatureLabel.setText(QCoreApplication.translate("MainWindow", u"Conductivity Temperature ", None))
        self.expirationDateLabel.setText(QCoreApplication.translate("MainWindow", u"Expiration Date", None))
        self.expirationDateDateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

