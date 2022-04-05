from email import message
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QSize
from pefile import PEFormatError


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
        self.scanButton.clicked.connect(self.scan)

    def open_dir(self):
        # dire = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        # print(dire)
        self.file_name, self.file_type = QFileDialog.getOpenFileName(self, "选取文件", "./")
        self.file_label.setText(self.file_name.split("/")[-1])

    def scan(self):
        messageBox = QMessageBox(self)

        try:
            result = True
            # result = MLScan(self.file_name) # MLScan就是真的scan函数
            messageBox.setWindowTitle("Result")
            if result:
                messageBox.setText("检测到病毒！")
            else:
                messageBox.setText("不是病毒!")
            messageBox.show()
        except PEFormatError:
            messageBox.setWindowTitle("Error")
            messageBox.setText("文件格式错误")
            messageBox.show()