# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoPlayer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_playVideo(object):
    def setupUi(self, playVideo):
        playVideo.setObjectName(_fromUtf8("playVideo"))
        playVideo.resize(680, 471)
        self.centralwidget = QtGui.QWidget(playVideo)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.centralwidget)
        self.videoPlayer.setGeometry(QtCore.QRect(200, 110, 300, 200))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        playVideo.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(playVideo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        playVideo.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(playVideo)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        playVideo.setStatusBar(self.statusbar)

        self.retranslateUi(playVideo)
        QtCore.QMetaObject.connectSlotsByName(playVideo)

    def retranslateUi(self, playVideo):
        playVideo.setWindowTitle(_translate("playVideo", "MainWindow", None))

from PyQt4 import phonon
