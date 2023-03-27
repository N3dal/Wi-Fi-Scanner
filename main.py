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

    class Signals(QObject):
        """
            Docstring;
        """

    pass


class MainWindow(QMainWindow):

    WIDTH, HEIGHT = 400, 600
    STYLESHEET = """
        background-color: #afc4e3;
    """
    PORT_SELECTION_STYLESHEET = """
        color: black;
    """
    CONNECT_BUTTON_STYLESHEET = """
        QPushButton{
            background-color: #d8e1ee;
            color: black;
            border-radius: 10px;
        }
        QPushButton:hover{
            background-color: #33b691;
        }
    """

    VIEW_IP_BUTTON_STYLESHEET = """
        QPushButton{
            background-color: #d8e1ee;
            color: black;
            border-radius: 10px;
        }
        QPushButton:hover{
            background-color: #33b691;
        }
    """
    TITLE = "Wi-Fi Scanner"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
        self.setStyleSheet(MainWindow.STYLESHEET)
        self.setWindowTitle(MainWindow.TITLE)

        self.port_selection = QComboBox(parent=self)
        self.port_selection.setStyleSheet(MainWindow.PORT_SELECTION_STYLESHEET)
        self.port_selection.move(10, 10)

        self.connect_button = QPushButton(parent=self, text="Connect")
        self.connect_button.setFixedSize(100, 30)
        self.connect_button.setStyleSheet(MainWindow.CONNECT_BUTTON_STYLESHEET)
        self.connect_button.clicked.connect(self.__connect_button_event)
        self.connect_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.connect_button.move(120, 10)

        self.view_ip_address_button = QPushButton(
            parent=self, text="View IP Address")
        self.view_ip_address_button.setFixedSize(160, 30)
        self.view_ip_address_button.setStyleSheet(
            MainWindow.VIEW_IP_BUTTON_STYLESHEET)
        self.view_ip_address_button.clicked.connect(
            self.__view_ip_address_button_event)
        self.view_ip_address_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.view_ip_address_button.move(230, 10)

    def __connect_button_event(self):
        """
            connect button event;

            return None;
        """

        return None

    def __view_ip_address_button_event(self):
        # todo: make sure that all docstring looks like this;
        """
            :ARGS:
            None

            :INFO:
            view ip address button event;

            :RETURNS:
            return None;
        """

        return None


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())

    return None


if __name__ == "__main__":
    main()
