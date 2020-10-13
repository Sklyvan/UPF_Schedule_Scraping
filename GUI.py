# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centersNames_Box = QtWidgets.QComboBox(self.centralwidget)
        self.centersNames_Box.setEnabled(False)
        self.centersNames_Box.setGeometry(QtCore.QRect(10, 10, 251, 22))
        self.centersNames_Box.setObjectName("centersNames_Box")
        self.degreesNames_Box = QtWidgets.QComboBox(self.centralwidget)
        self.degreesNames_Box.setEnabled(False)
        self.degreesNames_Box.setGeometry(QtCore.QRect(10, 50, 251, 22))
        self.degreesNames_Box.setObjectName("degreesNames_Box")
        self.gradesNames_Box = QtWidgets.QComboBox(self.centralwidget)
        self.gradesNames_Box.setEnabled(False)
        self.gradesNames_Box.setGeometry(QtCore.QRect(10, 90, 251, 22))
        self.gradesNames_Box.setObjectName("gradesNames_Box")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "MainWindow"))

    def generateCentersNames_Box(self, nOptions, optionsNames, isEnabled=True):
        for i in range(nOptions):
            self.centersNames_Box.addItem("")
            self.centersNames_Box.setItemText(i, self._translate("MainWindow", optionsNames[i]))
        self.centersNames_Box.setEnabled(isEnabled)

    def generateDegreesNames_Box(self, nOptions, optionsNames, isEnabled=True):
        for i in range(nOptions):
            self.degreesNames_Box.addItem('')
            self.degreesNames_Box.setItemText(i, self._translate('MainWindow', optionsNames[i]))
        self.degreesNames_Box.setEnabled(isEnabled)

    def genereateGradesNames_Box(self, nOptions, optionsNames, isEnabled=True):
        for i in range(nOptions):
            self.gradesNames_Box.addItem('')
            self.gradesNames_Box.setItemText(i, self._translate('MainWindow', optionsNames[i]))
        self.gradesNames_Box.setEnabled(isEnabled)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    UI = Ui_MainWindow()
    UI.setupUi(MainWindow)
    UI.generateCentersNames_Box(5, ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'])
    MainWindow.show()
    sys.exit(app.exec_())

