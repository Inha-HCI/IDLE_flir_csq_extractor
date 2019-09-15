from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(960,646)
        MainWindow.setStyleSheet("background-color: #1c1c1c")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.previewArea = QtWidgets.QPushButton(self.centralwidget)
        self.previewArea.setGeometry(QtCore.QRect(37, 182, 420, 357))
        self.previewArea.setStyleSheet("border-style: solid;\n"
"border-radius: 12px;\n"
"background-color:#434343;\n"
"color:white;\n"
"text-align: left;")
        self.previewArea.setText("")
        self.previewArea.setObjectName("previewArea")
        self.optionArea = QtWidgets.QPushButton(self.centralwidget)
        self.optionArea.setGeometry(QtCore.QRect(470, 182, 205, 357))
        self.optionArea.setStyleSheet("border-style: solid;\n"
"border-radius: 12px;\n"
"background-color:#434343;\n"
"color:white;\n"
"text-align: left;")
        self.optionArea.setText("")
        self.optionArea.setObjectName("optionArea")
        self.loadFileArea = QtWidgets.QPushButton(self.centralwidget)
        self.loadFileArea.setGeometry(QtCore.QRect(37, 104, 638, 67))
        self.loadFileArea.setStyleSheet("border-style: solid;\n"
"border-radius: 12px;\n"
"background-color:#434343;\n"
"color:white;\n"
"text-align: left;")
        self.loadFileArea.setText("")
        self.loadFileArea.setObjectName("loadFileArea")
        self.logo = QtWidgets.QPushButton(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(29, 17, 207, 65))
        self.logo.setStyleSheet("border-image:url(image/logo.png);\n"
"background-color:#00000000")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.outputArea = QtWidgets.QPushButton(self.centralwidget)
        self.outputArea.setGeometry(QtCore.QRect(686, 104, 238, 435))
        self.outputArea.setStyleSheet("border-style: solid;\n"
"border-radius: 12px;\n"
"background-color:#434343;\n"
"color:white;\n"
"text-align: left;")
        self.outputArea.setText("")
        self.outputArea.setObjectName("outputArea")
        self.progressArea = QtWidgets.QPushButton(self.centralwidget)
        self.progressArea.setGeometry(QtCore.QRect(37, 550, 775, 65))
        self.progressArea.setStyleSheet("border-style: solid;\n"
"border-radius: 12px;\n"
"background-color:#434343;\n"
"color:white;\n"
"text-align: left;")
        self.progressArea.setText("")
        self.progressArea.setObjectName("progressArea")
        self.extractBtn = QtWidgets.QPushButton(self.centralwidget)
        self.extractBtn.setGeometry(QtCore.QRect(822, 550, 102, 65))
        self.extractBtn.setStyleSheet("border-style: solid;\n"
"border-radius: 12px;\n"
"background-color:#ff8c00;\n"
"color:white;\n"
"text-align: center;")
        self.extractBtn.setObjectName("extractBtn")
        self.loadFileImage = QtWidgets.QPushButton(self.centralwidget)
        self.loadFileImage.setGeometry(QtCore.QRect(70, 120, 44, 36))
        self.loadFileImage.setStyleSheet("border-image:url(image/folder.png);\n"
"background-color:#00000000")
        self.loadFileImage.setText("")
        self.loadFileImage.setObjectName("loadFileImage")
        self.loadFileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadFileBtn.setGeometry(QtCore.QRect(129, 124, 77, 28))
        self.loadFileBtn.setStyleSheet("border-style: solid;\n"
"border-radius: 3px;\n"
"background-color:#ffffff;\n"
"color:#212121;\n"
"text-align: center;")
        self.loadFileBtn.setObjectName("loadFileBtn")
        self.previewLabel = QtWidgets.QLabel(self.centralwidget)
        self.previewLabel.setGeometry(QtCore.QRect(51, 192, 331, 31))
        self.previewLabel.setStyleSheet("background-color:#00000000;\n"
"color: #6dc8ff;")
        self.previewLabel.setObjectName("previewLabel")
        self.previewImg = QtWidgets.QPushButton(self.centralwidget)
        self.previewImg.setGeometry(QtCore.QRect(53, 228, 388, 291))
        self.previewImg.setStyleSheet("background-color: #000000")
        self.previewImg.setObjectName("previewImg")
        self.optionLabel = QtWidgets.QLabel(self.centralwidget)
        self.optionLabel.setGeometry(QtCore.QRect(481, 192, 181, 31))
        self.optionLabel.setStyleSheet("background-color:#00000000;\n"
"color: #6dc8ff;")
        self.optionLabel.setObjectName("optionLabel")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(697, 118, 181, 31))
        self.outputLabel.setStyleSheet("background-color:#00000000;\n"
"color: #6dc8ff;")
        self.outputLabel.setObjectName("outputLabel")
        self.skipLabel = QtWidgets.QLabel(self.centralwidget)
        self.skipLabel.setGeometry(QtCore.QRect(480, 230, 181, 31))
        self.skipLabel.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.skipLabel.setObjectName("skipLabel")
        self.formatLabel = QtWidgets.QLabel(self.centralwidget)
        self.formatLabel.setGeometry(QtCore.QRect(699, 156, 181, 31))
        self.formatLabel.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.formatLabel.setObjectName("formatLabel")
        self.normalizationLabel = QtWidgets.QLabel(self.centralwidget)
        self.normalizationLabel.setGeometry(QtCore.QRect(480, 355, 181, 31))
        self.normalizationLabel.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.normalizationLabel.setObjectName("normalizationLabel")
        self.skipValue = QtWidgets.QLineEdit(self.centralwidget)
        self.skipValue.setGeometry(QtCore.QRect(500, 296, 148, 24))
        self.skipValue.setStyleSheet("background-color:#ffffff;\n"
"color: #212121;\n"
"padding-left:5px;")
        self.skipValue.setObjectName("skipValue")
        self.filenameLabel = QtWidgets.QLabel(self.centralwidget)
        self.filenameLabel.setGeometry(QtCore.QRect(697, 397, 181, 31))
        self.filenameLabel.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.filenameLabel.setObjectName("filenameLabel")
        self.filenameValue = QtWidgets.QLineEdit(self.centralwidget)
        self.filenameValue.setGeometry(QtCore.QRect(697, 428, 216, 24))
        self.filenameValue.setStyleSheet("background-color:#ffffff;\n"
"color: #212121;\n"
"padding-left:5px;")
        self.filenameValue.setObjectName("filenameValue")
        self.savepathLabel = QtWidgets.QLabel(self.centralwidget)
        self.savepathLabel.setGeometry(QtCore.QRect(697, 462, 181, 31))
        self.savepathLabel.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.savepathLabel.setObjectName("savepathLabel")
        self.savepathValue = QtWidgets.QLineEdit(self.centralwidget)
        self.savepathValue.setGeometry(QtCore.QRect(697, 494, 216, 24))
        self.savepathValue.setStyleSheet("background-color:#ffffff;\n"
"color: #212121;\n"
"padding-left:5px;")
        self.savepathValue.setObjectName("savepathValue")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(48, 559, 752, 48))
        self.progressBar.setTextVisible(False)
        self.progressBar.setStyleSheet("QProgressBar:horizontal {\n"
"    border-radius: 7px;\n"
"    background: #212121;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background: #6dc8ff;\n"
"    border-radius: 7px;\n"
"}")
        self.progressBar.setProperty("value", 42)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.progressValue = QtWidgets.QPushButton(self.centralwidget)
        self.progressValue.setGeometry(QtCore.QRect(71, 550, 701, 65))
        self.progressValue.setStyleSheet("border-style: solid;\n"
"border-radius: 12px;\n"
"background-color:#00000000;\n"
"color:white;\n"
"text-align: center;")
        self.progressValue.setObjectName("progressValue")
        self.isSkip = QtWidgets.QCheckBox(self.centralwidget)
        self.isSkip.setGeometry(QtCore.QRect(482, 260, 181, 35))
        self.isSkip.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.isSkip.setObjectName("isSkip")
        self.normalizationBox = QtWidgets.QGroupBox(self.centralwidget)
        self.normalizationBox.setGeometry(QtCore.QRect(482, 388, 181, 141))
        self.normalizationBox.setStyleSheet("background-color:#00000000;\n"
"border-style: solid;")
        self.normalizationBox.setTitle("")
        self.normalizationBox.setObjectName("normalizationBox")
        self.isRaw = QtWidgets.QRadioButton(self.normalizationBox)
        self.isRaw.setGeometry(QtCore.QRect(0, 0, 181, 35))
        self.isRaw.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.isRaw.setChecked(True)
        self.isRaw.setObjectName("isRaw")
        self.isNormalize = QtWidgets.QRadioButton(self.normalizationBox)
        self.isNormalize.setGeometry(QtCore.QRect(0, 36, 181, 35))
        self.isNormalize.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.isNormalize.setObjectName("isNormalize")
        self.isBoth = QtWidgets.QRadioButton(self.normalizationBox)
        self.isBoth.setGeometry(QtCore.QRect(0, 72, 181, 35))
        self.isBoth.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.isBoth.setObjectName("isBoth")
        self.label_7 = QtWidgets.QLabel(self.normalizationBox)
        self.label_7.setGeometry(QtCore.QRect(19, 98, 141, 35))
        self.label_7.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.label_7.setObjectName("label_7")
        self.isFrame = QtWidgets.QCheckBox(self.centralwidget)
        self.isFrame.setGeometry(QtCore.QRect(696, 186, 181, 35))
        self.isFrame.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.isFrame.setChecked(True)
        self.isFrame.setObjectName("isFrame")
        self.isRawImage = QtWidgets.QCheckBox(self.centralwidget)
        self.isRawImage.setGeometry(QtCore.QRect(696, 220, 221, 35))
        self.isRawImage.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.isRawImage.setChecked(True)
        self.isRawImage.setObjectName("isRawImage")
        self.isGrayImage = QtWidgets.QCheckBox(self.centralwidget)
        self.isGrayImage.setGeometry(QtCore.QRect(696, 254, 221, 35))
        self.isGrayImage.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.isGrayImage.setChecked(True)
        self.isGrayImage.setObjectName("isGrayImage")
        self.isColorImage = QtWidgets.QCheckBox(self.centralwidget)
        self.isColorImage.setGeometry(QtCore.QRect(696, 288, 221, 35))
        self.isColorImage.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.isColorImage.setChecked(True)
        self.isColorImage.setObjectName("isColorImage")
        self.isRawData = QtWidgets.QCheckBox(self.centralwidget)
        self.isRawData.setGeometry(QtCore.QRect(696, 322, 221, 35))
        self.isRawData.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.isRawData.setChecked(True)
        self.isRawData.setObjectName("isRawData")
        self.isCelsiusData = QtWidgets.QCheckBox(self.centralwidget)
        self.isCelsiusData.setGeometry(QtCore.QRect(696, 356, 221, 35))
        self.isCelsiusData.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.isCelsiusData.setChecked(True)
        self.isCelsiusData.setObjectName("isCelsiusData")
        self.videoPathLabel = QtWidgets.QLabel(self.centralwidget)
        self.videoPathLabel.setGeometry(QtCore.QRect(220, 124, 441, 28))
        self.videoPathLabel.setStyleSheet("background-color:#00000000;\n"
"color: #ffffff;")
        self.videoPathLabel.setText("")
        self.videoPathLabel.setObjectName("videoPathLabel")
        self.outputArea.raise_()
        self.previewArea.raise_()
        self.optionArea.raise_()
        self.progressArea.raise_()
        self.loadFileArea.raise_()
        self.logo.raise_()
        self.extractBtn.raise_()
        self.loadFileImage.raise_()
        self.loadFileBtn.raise_()
        self.previewLabel.raise_()
        self.previewImg.raise_()
        self.optionLabel.raise_()
        self.outputLabel.raise_()
        self.skipLabel.raise_()
        self.formatLabel.raise_()
        self.normalizationLabel.raise_()
        self.skipValue.raise_()
        self.filenameLabel.raise_()
        self.filenameValue.raise_()
        self.savepathLabel.raise_()
        self.savepathValue.raise_()
        self.progressBar.raise_()
        self.progressValue.raise_()
        self.isSkip.raise_()
        self.normalizationBox.raise_()
        self.isFrame.raise_()
        self.isRawImage.raise_()
        self.isGrayImage.raise_()
        self.isColorImage.raise_()
        self.isRawData.raise_()
        self.isCelsiusData.raise_()
        self.videoPathLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IDLE Frame Maker ver 1.0"))
        self.extractBtn.setText(_translate("MainWindow", "EXTRACT"))
        self.loadFileBtn.setText(_translate("MainWindow", "OPEN"))
        self.previewLabel.setText(_translate("MainWindow", "PREVIEW"))
        self.previewImg.setText(_translate("MainWindow", "PushButton"))
        self.optionLabel.setText(_translate("MainWindow", "OPTION"))
        self.outputLabel.setText(_translate("MainWindow", "OUTPUT"))
        self.skipLabel.setText(_translate("MainWindow", "SKIP"))
        self.formatLabel.setText(_translate("MainWindow", "FORMAT"))
        self.normalizationLabel.setText(_translate("MainWindow", "NORMALIZATION"))
        self.skipValue.setText(_translate("MainWindow", "0"))
        self.filenameLabel.setText(_translate("MainWindow", "FILE NAME"))
        self.savepathLabel.setText(_translate("MainWindow", "SAVE PATH"))
        self.progressValue.setText(_translate("MainWindow", "EXTRACTING ... 42%"))
        self.isSkip.setText(_translate("MainWindow", "FRAME SKIP"))
        self.isRaw.setText(_translate("MainWindow", "RAW"))
        self.isNormalize.setText(_translate("MainWindow", "NORMALIZE"))
        self.isBoth.setText(_translate("MainWindow", "RAW ＆ "))
        self.label_7.setText(_translate("MainWindow", "NORMALIZE"))
        self.isFrame.setText(_translate("MainWindow", "FRAME (.fff)"))
        self.isRawImage.setText(_translate("MainWindow", "RAW IMAGE (.raw)"))
        self.isGrayImage.setText(_translate("MainWindow", "GRAY IMAGE (.png)"))
        self.isColorImage.setText(_translate("MainWindow", "COLOR IMAGE (.png)"))
        self.isRawData.setText(_translate("MainWindow", "RAW DATA (.csv)"))
        self.isCelsiusData.setText(_translate("MainWindow", "CELSIUS DATA (.csv)"))