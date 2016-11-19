import sys
import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.phonon import Phonon
from ui import Ui_MainWindow
from videoPlayerGui import Ui_playVideo
from PIL import Image

fp = 'test.jpg'
im = Image.open(fp, 'r')
w,h =  im.size
print w,h


class Video():
    def __init__(self, capture):
        self.capture = capture
        self.currentFrame = np.array([])

    def captureFrame(self):
        """
        capture frame and return captured frame
        """
        ret, readFrame = self.capture.read()
        return readFrame

    def captureNextFrame(self):
        """                           
        capture frame and reverse RBG BGR and return opencv image                                      
        """
        ret, readFrame = self.capture.read()
        if (ret == True):
            self.currentFrame = cv2.cvtColor(readFrame, cv2.COLOR_BGR2RGB)

    def convertFrame(self):
        """     converts frame to format suitable for QtGui            """
        try:
            height, width = self.currentFrame.shape[:2]
            img = QtGui.QImage(self.currentFrame,
                               width,
                               height,
                               QtGui.QImage.Format_RGB888)
            img = QtGui.QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None

    def convertSpecifiedFrame(frame):
        """     converts frame to format suitable for QtGui            """
        try:
            height, width = frame.shape[:2]
            img = QtGui.QImage(frame,
                               width,
                               height,
                               QtGui.QImage.Format_RGB888)
            img = QtGui.QPixmap.fromImage(img)
            return img
        except:
            return None

    def getImage(self):
        return cv2.imread("test.jpg")

    def addText(self, text):
        cv2.putText(self.currentFrame, text, (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)


class Gui(QtGui.QMainWindow):
    isCapture = False

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.vp = Ui_playVideo()
        self.ui.setupUi(self)
        self.video = Video(cv2.VideoCapture(0))
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()
        self.ui.btnCapture.clicked.connect(self.cb)
        self.ui.btnAddText.clicked.connect(self.addText)
        #self.vp.videoPlayer.
        self.ret, self.capturedFrame = self.video.capture.read()

    def cb(self):
        #       self.lookAtCam()
        #        QtCore.QTimer.singleShot(2000, lambda: self.ui.btnCapture.setEnabled(False))
        self.video.captureNextFrame()
        frame = self.video.convertFrame()
        self.ui.videoFrame_2.setPixmap(frame)
        self.ui.videoFrame_2.setScaledContents(True)

        self.capturedFrame = self.video.captureFrame()
        cv2.imwrite("test.jpg", self.capturedFrame)

        print 'captured'

    def addText(self):
        imText = self.video.getImage()
        imOrg = self.video.getImage()
        text = "%s" % self.ui.TextFieldAddText.text()
        cv2.putText(imText, text, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imwrite("testText.jpg", imText)
        pixmap = QtGui.QPixmap('testText.jpg')
        self.ui.videoFrame_2.setPixmap(pixmap)
        print 'Text added' + text

    def lookAtCam(self):
        self.video.captureNextFrame()
        self.video.addText('Look At camera !')
        self.ui.videoFrame.setPixmap(self.video.convertFrame())
        self.ui.videoFrame.setScaledContents(True)

    def play(self):
        try:
            if (get_idle_duration() < 5):
                self.ui.topLabel.setGeometry(QtCore.QRect(0, 0, 0,0))
                self.video.captureNextFrame()
                self.ui.videoFrame.setPixmap(self.video.convertFrame())
                self.ui.videoFrame.setScaledContents(True)

            else :
                self.ui.topLabel.setGeometry(QtCore.QRect(25, 22, 681, 521))
                pass
                #self.ui.topLabel.clear()
        except:
            print "No frame"


from ctypes import Structure, windll, c_uint, sizeof, byref

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Gui()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
