#!/usr/bin/python3
# -----------------------------------------------------------------
# view all available wifi networks from esp32;
#
#
#
# Author:N84.
#
# Create Date:Mon Mar 27 02:28:55 2023.
# ///
# ///
# ///
# -----------------------------------------------------------------


import serial
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utils import *


class WifiLabel(QWidget):
    """
        custom wifi label;
        that display the network name and other status;
    """

    pass


class MainWindow(QMainWindow):

    WIDTH, HEIGHT = 400, 600
    STYLESHEET = """
        background-color: #afc4e3;
    """
    TITLE = "Wi-Fi Scanner"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
        self.setStyleSheet(MainWindow.STYLESHEET)
        self.setWindowTitle(MainWindow.TITLE)


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())

    return None


if __name__ == "__main__":
    main()
