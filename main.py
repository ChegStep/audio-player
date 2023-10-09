

import des
from mutagen.mp3 import MP3
from PySide6 import QtWidgets, QtGui, QtMultimedia, QtCore
import os
import sys

class Player(QtWidgets.QMainWindow, des.Ui_MainWindow):
    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)
        self.media_player = QtMultimedia.QMediaPlayer()
        #bttns
        self.btnPlay.clicked.connect(self.play_music)
        self.btnPause.clicked.connect(self.pause)
        self.btnNext.clicked.connect(self.play_next)
        self.btnBack.clicked.connect(self.play_back)
        self.listWidget.itemDoubleClicked.connect(self.play_current_music)
        self.btnAddAudio.clicked.connect(self.load)
        self.btnPause.hide()
        #sliders
        self.volumeSlider.setValue(50)
        self.volumeSlider.valueChanged.connect(self.setVolume)
        #other
        self.dir = ' '
        self.aOutput = QtMultimedia.QAudioOutput(parent=self)
        self.aOutput.setVolume(0.5)
        self.flag = 0

    def initPlayer(self, state):
        audio = MP3(self.file_name)
        min, secs = self.duration_detector(audio.info.length)
        if state == QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia:
            self.play_next()
        self.timeEndMus.setText('{}:{}'.format(min, secs))

    def duration_detector(self, length):
        mins = length // 60  # calculate in minutes
        length %= 60
        seconds = length  # calculate in seconds

        return int(mins), int(seconds)

    def play_current_music(self):
        self.btnPause.show()
        self.btnPlay.hide()
        self.media_player = QtMultimedia.QMediaPlayer()
        self.item = self.listWidget.currentItem()
        self.newit = self.listWidget.currentRow()
        self.file_name = os.path.join(self.dir, self.item.text())
        self.songName.setText("Играет: " + self.item.text().removesuffix('.mp3'))
        self.media_player.setAudioOutput(self.aOutput)
        self.media_player.setSource(QtCore.QUrl.fromLocalFile(self.file_name))
        self.musicSlider.setMinimum(0)
        self.musicSlider.setMaximum(self.media_player.duration())
        self.musicSlider.sliderMoved.connect(self.media_player.setPosition)
        self.media_player.positionChanged.connect(self.musicSlider.setValue)
        self.media_player.mediaStatusChanged.connect(self.initPlayer)
        self.musicSlider.show()
        self.music_ic.show()
        self.volumeSlider.show()
        self.volume_ic.show()
        self.timeNowMus.show()
        self.timeEndMus.show()
        self.songName.show()
        self.musicSlider.valueChanged[int].connect(self.time_value)
        self.media_player.play()

    def time_value(self):
        minutes, seconds = divmod(self.musicSlider.value()/ 1000, 60)
        self.timeNowMus.setText(f'{minutes:0>2.0f}:{seconds:0>2.0f}')

    def play_music(self):
        if self.dir == ' ':
            self.load()
        else:
            if self.flag == 0:
                self.listWidget.setCurrentRow(0)
                self.play_current_music()
            elif self.flag == 1:
                self.media_player.play()
                self.btnPause.show()
                self.btnPlay.hide()

    def pause(self):
        self.media_player.pause()
        self.flag = 1
        self.btnPause.hide()
        self.btnPlay.show()

    def play_next(self):
        if self.newit + 1 >= self.countOfList:
            self.listWidget.setCurrentRow(0)
        else:
            self.listWidget.setCurrentRow(self.newit + 1)
        self.play_current_music()

    def play_back(self):
        if self.newit - 1 <= -1:
            self.listWidget.setCurrentRow(self.countOfList - 1)
        else:
            self.listWidget.setCurrentRow(self.newit - 1)
        self.play_current_music()

    def load(self):
        self.listWidget.clear()

        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")

        if dir:
            for file_name in os.listdir(dir):
                if file_name.endswith(".mp3"):
                    self.listWidget.addItem(os.path.join(file_name))
            self.dir = dir
        self.countOfList = self.listWidget.count()

    def setVolume(self, value):
        self.aOutput.setVolume(value / 100)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open("style.css", "r") as file:
        app.setStyleSheet(file.read())
    win = Player()
    win.show()
    sys.exit(app.exec())