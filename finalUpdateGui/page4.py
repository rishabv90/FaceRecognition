# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\risha\OneDrive\Desktop\faceRecGui\guiTest\guitTest1\page6.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 899)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(470, 180, 651, 581))
        self.graphicsView.setObjectName("graphicsView")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 270, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 720, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(240, 370, 91, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(360, 370, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 320, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 210, 211, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 410, 401, 161))
        self.label_10.setObjectName("label_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 560, 211, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 720, 151, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 361, 61))
        self.label_2.setObjectName("label_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1000, 10, 111, 51))
        self.label_11.setStyleSheet("image: url(samPicture.jpg);")
        self.label_11.setText("")
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setPixmap(QtGui.QPixmap("samPicture.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 190, 221, 61))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 250, 221, 61))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 300, 221, 61))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 350, 221, 61))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(30, 610, 251, 61))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(320, 610, 251, 61))
        self.label_17.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 21))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.radioButton.setText(_translate("MainWindow", "Administrative"))
        self.radioButton_2.setText(_translate("MainWindow", "Regular User"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Instructions:- </span></p><p><span style=\" font-size:12pt;\">- Please get ready to get 25 clear pictures clcicked. </span></p><p><span style=\" font-size:12pt;\">- Please present a clear view to the camera.</span></p><p><span style=\" font-size:12pt;\">- Please provide variation by Left/Right head movement.</span></p><p><br/></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Begin face Recognition Collection"))
        self.pushButton_5.setText(_translate("MainWindow", "Cancel"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Administravtive Login</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your name :</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your password :</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your username :</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your Status :</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Face recognition collection status :</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">XX/25</span></p></body></html>"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
