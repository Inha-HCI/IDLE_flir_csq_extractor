from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from script import bin_utils
from script import raw2celsius
from script import image2csv
from script import csv2colorimg
import idle
import os
import glob
from shutil import rmtree

##### Method ###################################################################################################################

class idleProject(QObject):
    # signal
    pSignal = pyqtSignal(int, str) # progressbar
    aSignal = pyqtSignal(bool) # active or not

    # 프로그램 내 사용하는 변수 선언&초기화
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.test = idle.Ui_MainWindow()
        self.test.setupUi(MainWindow)
        self.videoFilePath = None

        # thread
        self.th = Worker(parent=self)

        # 프로그램 내 폰트 등록
        QFontDatabase.addApplicationFont("font/NanumSquareEB_0.ttf")
        QFontDatabase.addApplicationFont("font/NanumSquareB_0.ttf")
        QFontDatabase.addApplicationFont("font/NanumSquareL_0.ttf")
        QFontDatabase.addApplicationFont("font/NanumSquareR_0.ttf")

        font = QFont("나눔스퀘어 Bold", 12)
        self.test.loadFileBtn.setFont(font)
        font = QFont("나눔스퀘어", 12)
        self.test.videoPathLabel.setFont(font)

        font = QFont("나눔스퀘어 ExtraBold", 19)
        self.test.previewLabel.setFont(font)
        self.test.optionLabel.setFont(font)
        self.test.outputLabel.setFont(font)
        self.test.skipLabel.setFont(font)

        font = QFont("나눔스퀘어 ExtraBold", 15)
        self.test.skipLabel.setFont(font)
        self.test.normalizationLabel.setFont(font)
        self.test.formatLabel.setFont(font)
        self.test.filenameLabel.setFont(font)
        self.test.savepathLabel.setFont(font)

        font = QFont("나눔스퀘어", 14)
        self.test.skipValue.setFont(font)
        self.test.filenameValue.setFont(font)
        self.test.savepathValue.setFont(font)

        font = QFont("나눔스퀘어", 16)
        self.test.isSkip.setFont(font)
        self.test.isRaw.setFont(font)
        self.test.isNormalize.setFont(font)
        self.test.isBoth.setFont(font)
        self.test.label_7.setFont(font)
        self.test.isFrame.setFont(font)
        self.test.isRawImage.setFont(font)
        self.test.isGrayImage.setFont(font)
        self.test.isColorImage.setFont(font)
        self.test.isRawData.setFont(font)
        self.test.isCelsiusData.setFont(font)

        font = QFont("나눔스퀘어 ExtraBold", 14)
        self.test.progressValue.setFont(font)
        self.test.extractBtn.setFont(font)

        # Option Part 값
        self.isFrameSkip = False
        self.frameSkipValue = 1
        self.normalizationValue = 1  # 1 = Raw / 2 = Normalize / 3 = Raw & Normalize

        # Output Part 값 1
        self.isFrame = False
        self.isRawImage = False
        self.isGrayImage = False
        self.isColorImage = False
        self.isRawData = False
        self.isCelsiusData = False

        # Output Part 값 2
        self.fileName = None
        self.savePath = None

    # 프로그램 구동 메소드
    def start(self):
        self.setProgressbar(0, "Select your .csq file")
        self.test.loadFileBtn.clicked.connect(self.loadVideo)
        self.test.extractBtn.clicked.connect(self.extract)

        self.pSignal.connect(self.updateProgressbar)
        self.aSignal.connect(self.disableGUI)

    def updateProgressbar(self, progress, msg):
        self.setProgressbar(progress, msg)

    def disableGUI(self, disable):
        if disable:
            self.disableWidget()
        else:
            self.enableWidget()

    # 이미지를 인자로 받아 Preview Part에 띄워주는 메소드
    def setPreviewImage(self, imagePath):
        self.test.previewImg.setText("")
        self.test.previewImg.setStyleSheet("background-color: #000000;\nborder-image:url(" + imagePath + ");")

    # 정수를 인자로 받아 Progress Bar를 핸들링하는 메소드
    def setProgressbar(self, num, text):
        # if text is None:
        #     tmp = "EXTRACTING ... " + str(num) + "%" #TODO
        self.test.progressBar.setValue(num)
        self.test.progressValue.setText(text)
       

    def disableWidget(self):
        self.test.loadFileBtn.setEnabled(False)
        self.test.isSkip.setEnabled(False)
        self.test.skipValue.setEnabled(False)
        self.test.isRaw.setEnabled(False)
        self.test.isNormalize.setEnabled(False)
        self.test.isBoth.setEnabled(False)
        self.test.isFrame.setEnabled(False)
        self.test.isRawImage.setEnabled(False)
        self.test.isGrayImage.setEnabled(False)
        self.test.isColorImage.setEnabled(False)
        self.test.isRawData.setEnabled(False)
        self.test.isCelsiusData.setEnabled(False)
        self.test.filenameValue.setEnabled(False)
        self.test.savepathValue.setEnabled(False)

    def enableWidget(self):
        self.test.loadFileBtn.setEnabled(True)
        self.test.isSkip.setEnabled(True)
        self.test.skipValue.setEnabled(True)
        self.test.isRaw.setEnabled(True)
        self.test.isNormalize.setEnabled(True)
        self.test.isBoth.setEnabled(True)
        self.test.isFrame.setEnabled(True)
        self.test.isRawImage.setEnabled(True)
        self.test.isGrayImage.setEnabled(True)
        self.test.isColorImage.setEnabled(True)
        self.test.isRawData.setEnabled(True)
        self.test.isCelsiusData.setEnabled(True)
        self.test.filenameValue.setEnabled(True)
        self.test.savepathValue.setEnabled(True)

    ##### Slots ####################################################################################################################

    # 파일탐색기를 열어 비디오를 선택하고 해당 경로를 저장함
    def loadVideo(self):
        self.videoFilePath = QFileDialog.getOpenFileName(None, "Open File", "./", "File (*.*)")
        self.test.videoPathLabel.setText(self.videoFilePath[0])
        self.test.savepathValue.setText(QFileInfo(self.videoFilePath[0]).path())

        #setPreview
        try:
            os.makedirs('tmp')
        except FileExistsError:
            pass
        
        # extract first frame and set preview
        bin_utils.exec_os("./bin/exiftool {0} -b -RawThermalImage > ./tmp/preview.raw".format(self.videoFilePath[0]))
        bin_utils.exec_os("./bin/ffmpeg -y -f image2 -vcodec jpegls -i ./tmp/preview.raw -f image2 -vcodec png ./tmp/preview.png")
        image2csv.image2csv('./tmp/preview.png', './tmp/')
        raw2celsius.raw2celsius('./tmp/preview.csv', './tmp/', 'preview_celsius')
        csv2colorimg.csv2colorimg('./tmp/preview_celsius.csv', './tmp/')
        self.setPreviewImage('./tmp/preview_celsius.png')

    # Extract 버튼 클릭 이벤트 처리
    def extract(self):
        
        # Frame Skip 체크박스 체크 여부와 값
        if self.test.isSkip.isChecked():
            self.isFrameSkip = True
            self.frameSkipValue = int(self.test.skipValue.text())
        else :
            self.isFrameSkip = False
            self.frameSkipValue = 0

        # Normalization 라디오 버튼 체크된 버튼 여부와 값 지정
        if self.test.isRaw.isChecked():
            self.normalizationValue = 1
        elif self.test.isNormalize.isChecked():
            self.normalizationValue = 2
        elif self.test.isBoth.isChecked():
            self.normalizationValue = 3

        # Format 체크박스들의 체크 여부
        if self.test.isFrame.isChecked():
            self.isFrame = True
        else :
            self.isFrame = False
        if self.test.isRawImage.isChecked():
            self.isRawImage = True
        else :
            self.isRawImage = False
        if self.test.isGrayImage.isChecked():
            self.isGrayImage = True
        else :
            self.isGrayImage = False
        if self.test.isColorImage.isChecked():
            self.isColorImage = True
        else :
            self.isColorImage = False
        if self.test.isRawData.isChecked():
            self.isRawData = True
        else :
            self.isRawData = False    
        if self.test.isCelsiusData.isChecked():
            self.isCelsiusData = True
        else :
            self.isCelsiusData = False

        # File Name과 Save Path 읽어오기
        self.videoFile = self.videoFilePath[0]
        self.fileName = self.test.filenameValue.text()
        self.savePath = self.test.savepathValue.text()
        
        # 메소드 값 초기 설정
        # self.setProgressbar(0, 'init')

        ########################################
        ##            extract data            ##
        ########################################
        option = {}
        
        baseName = os.path.basename(self.videoFile)
        baseName = os.path.splitext(baseName)[0]
        
        save_dirs = {}
        save_dirs['fff'] = os.path.join(self.savePath, baseName, 'fff')
        save_dirs['raw'] = os.path.join(self.savePath, baseName, 'raw')
        save_dirs['png_raw'] = os.path.join(self.savePath, baseName, 'png_raw')
        save_dirs['png_color'] = os.path.join(self.savePath, baseName, 'png_color')
        save_dirs['csv_raw'] = os.path.join(self.savePath, baseName, 'csv_raw')
        save_dirs['csv_celsius'] = os.path.join(self.savePath, baseName, 'csv_celsius')
        
        isSelected = {}
        isSelected['fff'] = self.isFrame
        isSelected['raw'] = self.isRawImage
        isSelected['png_raw'] = self.isGrayImage
        isSelected['png_color'] = self.isColorImage
        isSelected['csv_raw'] = self.isRawData
        isSelected['csv_celsius'] = self.isCelsiusData
        
        frameInc = 1
        if self.isFrameSkip:
            frameInc = self.frameSkipValue
            if frameInc < 1:
                frameInc = 1
        int2Index = lambda idx : '%05d' % (int(idx))
        
        # pack Options
        option['fileName'] = self.fileName
        option['baseName'] = os.path.splitext(baseName)[0]
        option['save_dirs'] = save_dirs
        option['isSelected'] = isSelected
        option['frameInc'] = frameInc
        option['int2Index'] = int2Index

        self.th.setOption(option)
        self.th.working = True
        self.th.start()
        return

class Worker(QThread):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.working = True
        self.option = None
    
    def setOption(self, option):
        self.option = option

    def updateProgressbar(self, progress, msg):
        self.parent.pSignal.emit(progress, msg)

    def disableGUI(self, disable):
        self.parent.aSignal.emit(disable)

    def run(self):
        # disable Widget
        self.disableGUI(True)

        # unpack data
        fileName = self.option['fileName']
        save_dirs = self.option['save_dirs']
        isSelected = self.option['isSelected']
        frameInc = self.option['frameInc']
        int2Index = self.option['int2Index']

        # Calculate progress data
        numList = len(glob.glob(save_dirs['fff']+'/*.fff'))
        cur = 0
        all = (numList/frameInc) * 5

        for dir in save_dirs.values():
            os.makedirs(dir, exist_ok=True)

        # self.test.progressValue.setText("Splitting Frames ... ")
        self.updateProgressbar(0, "Splitting Frames ... ")
        # command = "./bin/perl -f ./script/split.pl -i {0} -o {1} -b {2} -p fff -x fff".format(self.videoFile, save_dirs['fff'], self.fileName)
        # bin_utils.exec_os(command)
        
        # .fff to .raw
        for idx in range(frameInc, numList+1, frameInc):
            name = fileName + int2Index(idx)
            input_name = os.path.join(save_dirs['fff'], name+'.fff')
            output_name = os.path.join(save_dirs['raw'], name+'.raw')
            bin_utils.exec_os("./bin/exiftool {0} -b -RawThermalImage > {1}".format(input_name, output_name))
            #update progressbar
            cur+=1
            precent = int((cur/all)*100)
            self.updateProgressbar(precent, "EXTRACTING ... " + str(precent) + "%")

        # .raw to .png(raw)
        for idx in range(frameInc, numList+1, frameInc):
            name = fileName + int2Index(idx)
            input_name = os.path.join(save_dirs['raw'], name+'.raw')
            output_name = os.path.join(save_dirs['png_raw'], name+'.png')
            bin_utils.exec_os("./bin/ffmpeg -y -f image2 -vcodec jpegls -i {0} -f image2 -vcodec png {1}".format(input_name, output_name))
            #update progressbar
            cur+=1
            precent = int((cur/all)*100)
            self.updateProgressbar(precent, "EXTRACTING ... " + str(precent) + "%")

        self.updateProgressbar(50, "test")

        # .png(raw) to .csv(raw)    
        for idx in range(frameInc, numList+1, frameInc):
            name = fileName + int2Index(idx)
            input_name = os.path.join(save_dirs['png_raw'], name+'.png')
            image2csv.image2csv(input_name, save_dirs['csv_raw']+'/')
            #update progressbar
            cur+=1
            precent = int((cur/all)*100)
            self.updateProgressbar(precent, "EXTRACTING ... " + str(precent) + "%")

        # .csv(raw) to .csv(celsius)
        for idx in range(frameInc, numList+1, frameInc):
            name = fileName + int2Index(idx)
            input_name = os.path.join(save_dirs['csv_raw'], name+'.csv')
            raw2celsius.raw2celsius(input_name, save_dirs['csv_celsius'])
            #update progressbar
            cur+=1
            precent = int((cur/all)*100)
            self.updateProgressbar(precent, "EXTRACTING ... " + str(precent) + "%")

        # .csv(celsius) to .png(rgb)
        for idx in range(frameInc, numList+1, frameInc):
            name = fileName + int2Index(idx)
            input_name = os.path.join(save_dirs['csv_celsius'], name+'.csv')
            csv2colorimg.csv2colorimg(input_name, save_dirs['png_color'])
            #update progressbar
            cur+=1
            precent = int((cur/all)*100)
            self.updateProgressbar(precent, "EXTRACTING ... " + str(precent) + "%")

        # remove unselected files
        for category, selected in isSelected.items():
            if not selected:
                rmtree(save_dirs[category])

        self.disableGUI(False)
        



##### Main #####################################################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    idle = idleProject()
    idle.start()

    MainWindow.show()
    sys.exit(app.exec_())
