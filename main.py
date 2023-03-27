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
from serial.tools import list_ports
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utils import *


class SerialHandler:
    """
        Docstring;
    """

    BUAD_RATES = [300,
                  600,
                  750,
                  1200,
                  2400,
                  4800,
                  9600,
                  19200,
                  31250,
                  38400,
                  57600,
                  74880,
                  115200,
                  230400,
                  250000,
                  460800,
                  500000,
                  921600,
                  1000000,
                  2000000]

    class Signals(QObject):
        """
            Docstring;
        """

    def __init__(self):

        self.__available_ports = []
        self.__active_connections = []

    def check_for_available_ports(self):
        """
            :ARGS:
                None;

            :INFO:
                check out from the available ports on the machine;

            :RETURNS:
                return list;
        """

        self.__available_ports = list_ports.comports()
        print(self.__available_ports)

        return self.__available_ports

    def open_connection(self, device_name: str, buad_rate: int, timeout: int = 1):
        """
            :ARGS:
                device_name: str => the device name or path;
                buad_rate: int => data buad rate;
                timeout:int => timeout;

            :INFO:
                create a serial connection simply out open serial communication;

            :RETURNS:
                return None;
        """

        try:
            conn = serial.Serial(device_name, int(buad_rate), timeout=timeout)
            self.__active_connections.append(conn)

        except:
            raise Exception(
                f"Can't open the port {device_name=} with buad_rate {baudrate=}")

        return None

    def close_connection(self, device_name: str):
        """
            :ARGS:
                device_name:str => the device that we want to close;

            :INFO:
                close the serial connection for specific device;

            :RETURNS:
                return bool;

                return True if the device closed, other wise it returns False;
        """

        if not self.__active_connections:
            # if theres no connections;
            return False

        for conn in self.__active_connections.copy():
            if conn.name == device_name:
                conn.close()

                # now remove the conn from the active list;
                self.__active_connections.remove(conn)
                return True

        return False

    def close_all(self):
        """
            :ARGS:
                None;

            :INFO:
                close all the active connections;

            :RETURNS:
                return None;

        """

        for conn in self.__active_connections.copy():
            self.close_connection(conn.name)

        self.__active_connections.clear()

        return None

    @property
    def available_ports(self):
        """
            Docstring;
        """

        # first check out for available ports;
        self.check_for_available_ports()

        return self.__available_ports

    @property
    def active_connections(self):
        """
            View all available connections;
        """

        return self.__active_connections


class WifiLabel(QFrame):
    """
        custom wifi label;
        that display the network name and other status;
    """

    WIDTH, HEIGHT = 390, 40
    STYLESHEET = """
        background-color: #d8e1ee;
        color: black;
    """

    class Signals(QObject):
        """
            Docstring;
        """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(WifiLabel.WIDTH, WifiLabel.HEIGHT)
        self.setStyleSheet(WifiLabel.STYLESHEET)
        self.show()

    def change_background_color(self, color: str):
        """
            docstring;
        """

        stylesheet = f"""
            background-color: {color};
            color: black;
        """

        self.setStyleSheet(stylesheet)

        return None


class MainWindow(QMainWindow):

    WIDTH, HEIGHT = 400, 600
    STYLESHEET = """
        background-color: #afc4e3;
    """
    PORT_SELECTION_STYLESHEET = """
        color: black;
    """

    BUAD_RATE_SELECTION_STYLESHEET = """
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

        self.serial_handler = SerialHandler()

        self.port_selection = QComboBox(parent=self)
        self.port_selection.setStyleSheet(MainWindow.PORT_SELECTION_STYLESHEET)
        self.port_selection.addItems(
            port.device for port in self.serial_handler.available_ports)
        self.port_selection.move(10, 10)

        self.buad_rate_selection = QComboBox(parent=self)
        self.buad_rate_selection.setStyleSheet(
            MainWindow.PORT_SELECTION_STYLESHEET)
        self.buad_rate_selection.addItems(
            str(buad_rate) for buad_rate in self.serial_handler.BUAD_RATES)
        self.buad_rate_selection.move(10, 50)

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

        start = 95

        for _ in range(10):
            self.wifi = WifiLabel(parent=self)
            self.wifi.move(5, start)
            start += 45

    def __connect_button_event(self):
        """
            connect button event;

            return None;
        """

        if self.connect_button.text() == "Connect":
            self.connect_button.setText("Disconnect")

            device_name = self.port_selection.currentText()
            buad_rate = self.buad_rate_selection.currentText()

            # now open serial Connection;
            self.serial_handler.open_connection(
                device_name=device_name, buad_rate=buad_rate)

        else:
            self.connect_button.setText("Connect")
            self.serial_handler.close_all()

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
