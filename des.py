# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)
import res_ic

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 526)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/icons/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: #ffffff;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 12pt;\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    border-radius: 4px;\n"
"    background: white;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #fff;\n"
"    border: 1px solid gray;\n"
"    width: 10px;\n"
"    margin: -5px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::sub-page:qlineargradient {\n"
"    background: gray;\n"
"    border-radius: 4px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Rubik"])
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 30px")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.btnAddAudio = QPushButton(self.centralwidget)
        self.btnAddAudio.setObjectName(u"btnAddAudio")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnAddAudio.sizePolicy().hasHeightForWidth())
        self.btnAddAudio.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAddAudio.setIcon(icon1)
        self.btnAddAudio.setIconSize(QSize(14, 14))

        self.horizontalLayout_2.addWidget(self.btnAddAudio)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setAlignment(Qt.AlignCenter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"font-size: 16px")

        self.verticalLayout.addWidget(self.listWidget)

        self.songName = QLabel(self.centralwidget)
        self.songName.setObjectName(u"songName")

        self.verticalLayout.addWidget(self.songName)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setAlignment(Qt.AlignCenter)
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBack.setIcon(icon2)
        self.btnBack.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btnBack)

        self.btnPlay = QPushButton(self.centralwidget)
        self.btnPlay.setObjectName(u"btnPlay")
        self.btnPlay.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPlay.setIcon(icon3)
        self.btnPlay.setIconSize(QSize(45, 45))
        self.btnPlay.setStyleSheet(u"margin-left: 15px;"
                                    "	margin-right: 15px;\n")

        self.horizontalLayout.addWidget(self.btnPlay)

        self.btnPause = QPushButton(self.centralwidget)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/pause.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPause.setIcon(icon4)
        self.btnPause.setIconSize(QSize(45, 45))
        self.btnPause.setStyleSheet(u"margin-left: 15px;"
                                      "	margin-right: 15px;\n")

        self.horizontalLayout.addWidget(self.btnPause)

        self.btnNext = QPushButton(self.centralwidget)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/next.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNext.setIcon(icon5)
        self.btnNext.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btnNext)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.music_ic = QLabel(self.centralwidget)
        self.music_ic.setObjectName(u"music_ic")
        self.music_ic.setEnabled(False)
        sizePolicy.setHeightForWidth(self.music_ic.sizePolicy().hasHeightForWidth())
        self.music_ic.setSizePolicy(sizePolicy)
        self.music_ic.setMaximumSize(QSize(20, 20))
        self.music_ic.setPixmap(QPixmap(u":/icons/icons/music.svg"))
        self.music_ic.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.music_ic)

        self.timeNowMus = QLabel(self.centralwidget)
        self.timeNowMus.setObjectName(u"timeNowMus")
        self.timeNowMus.setStyleSheet(u"margin-left: 5px;"
"	font-size: 12px;\n")

        self.horizontalLayout_3.addWidget(self.timeNowMus)

        self.musicSlider = QSlider(self.centralwidget)
        self.musicSlider.setObjectName(u"musicSlider")
        self.musicSlider.setOrientation(Qt.Horizontal)
        self.musicSlider.setInvertedAppearance(False)
        self.musicSlider.setInvertedControls(False)

        self.horizontalLayout_3.addWidget(self.musicSlider)

        self.timeEndMus = QLabel(self.centralwidget)
        self.timeEndMus.setObjectName(u"timeEndMus")
        self.timeEndMus.setStyleSheet(u"margin-right: 10px;\n"
"	font-size: 12px;\n")
        self.timeEndMus.setOpenExternalLinks(False)

        self.horizontalLayout_3.addWidget(self.timeEndMus)

        self.volume_ic = QLabel(self.centralwidget)
        self.volume_ic.setObjectName(u"volume_ic")
        self.volume_ic.setMaximumSize(QSize(20, 20))
        self.volume_ic.setStyleSheet(u"")
        self.volume_ic.setPixmap(QPixmap(u":/icons/icons/volume.svg"))
        self.volume_ic.setScaledContents(True)
        self.volume_ic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.volume_ic.setIndent(-1)

        self.horizontalLayout_3.addWidget(self.volume_ic)

        self.volumeSlider = QSlider(self.centralwidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximumSize(QSize(50, 16777215))
        self.volumeSlider.setStyleSheet(u"")
        self.volumeSlider.setTracking(True)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.volumeSlider)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Music Player", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MP3 PLAYER", None))
        self.btnAddAudio.setText("")
        self.songName.setText("")
        self.btnBack.setText("")
        self.btnPlay.setText("")
        self.btnPause.setText("")
        self.btnNext.setText("")
        self.music_ic.setText("")
        self.timeNowMus.setText("")
        self.timeEndMus.setText("")
        self.volume_ic.setText("")
        self.musicSlider.hide()
        self.music_ic.hide()
        self.volumeSlider.hide()
        self.volume_ic.hide()
        self.timeNowMus.hide()
        self.timeEndMus.hide()
        self.songName.hide()
    # retranslateUi

