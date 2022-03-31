# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from PyQt5.QtWidgets import QApplication

from main_window import main_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec_()
