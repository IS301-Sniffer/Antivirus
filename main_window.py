from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from scanner_window import Ui_MainWindow


class main_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(main_window, self).__init__(parent)
        self.file_name = ""
        self.file_type = ""
        self.setupUi(self)
        self.file_label.setWordWrap(True) # 允许label换行
        self.setWindowIcon(QIcon(QPixmap("/home/virus/test/resources/images/virus_icon.png"))) # 这里图片是绝对路径，可以根据需要进行修改
        self.configure_button()

    def configure_button(self):
        self.openButton.clicked.connect(self.open_dir)

    def open_dir(self):
        # dire = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        # print(dire)
        self.file_name, self.file_type = QFileDialog.getOpenFileName(self, "选取文件", "./")
        self.file_label.setText(self.file_name.split("/")[-1])