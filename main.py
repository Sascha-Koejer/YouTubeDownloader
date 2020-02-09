import sys
import os
import queue
from pytube import YouTube
from configparser import  ConfigParser
from qtpy import QtWidgets
from YTDownloader.mainwindow import Ui_MainWindow
from PyQt5.QtCore import QThread, pyqtSignal


settings_folder = os.path.expandvars(R"C:\Users\$USERNAME\Documents\YTDownloader")
settings_path = os.path.expandvars(R"C:\Users\$USERNAME\Documents\YTDownloader\settings.ini")
config = ConfigParser()
q = queue.PriorityQueue()

if os.path.isfile(settings_path) != True:
    config["Settings"] = {
        "path" : "."
    }
    if os.path.exists(settings_folder) != True:
        os.mkdir(os.path.expandvars(settings_folder))
    with open(settings_path, "w") as configfile:
        config.write(configfile)

config.read(settings_path)

app = QtWidgets.QApplication(sys.argv)
max_file_size = 0

class MainWindow(QtWidgets.QMainWindow):
    urlChanged = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_download_path.triggered.connect(self.change_dir)
        self.ui.progressBar.setMaximum(1)

        self.ui.addbutton.clicked.connect(self.add_waitinglist)
        self.ui.downloadbutton.clicked.connect(self.start_download)
        
    def add_waitinglist(self):
        url = self.ui.urlinput.text()
        yt = YouTube(url)
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        qualtiy = 140
        self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("Audio"))
        if self.ui.checkBox.isChecked():
            qualtiy = 18
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("Video"))
        self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(yt.title))
        self.ui.urlinput.clear()
        q.put((qualtiy, url))
        
    def start_download(self):
        self.calc = Download()
        self.calc.valueChanged.connect(self.change_progress)
        self.calc.start()
        
    def change_progress(self, value):
        self.ui.progressBar.setMinimum(-max_file_size)
        if value == 0:
            self.ui.urlinput.clear()
            self.ui.progressBar.setValue(1)
        self.ui.progressBar.setValue(-value)
        
    def change_dir(self):
        dir_ = QtWidgets.QFileDialog.getExistingDirectory(None, 'Choose a Folder:', config.get('Settings', 'path'), QtWidgets.QFileDialog.ShowDirsOnly)
        config.set("Settings", "path", dir_)
        with open(settings_path, "w") as configfile:
            config.write(configfile)

class Download(QThread):

    valueChanged = pyqtSignal(int)

    def run(self, *params):
        try:
            while not q.empty():
                video = q.get()
                print(video)
                yt = YouTube(video[1], on_progress_callback = self.in_progress, on_complete_callback = self.run)
                stream = yt.streams.get_by_itag(video[0])

                global max_file_size
                max_file_size = stream.filesize
                stream.download(config.get('Settings', 'path'))
                self.valueChanged.emit(0)

        except BaseException as error:
            print('An exception occurred: {}'.format(error))

    def in_progress(self, stream, unknown, buffer, bytes_left):
        self.valueChanged.emit(bytes_left)

window = MainWindow()
window.show()

sys.exit(app.exec_())
