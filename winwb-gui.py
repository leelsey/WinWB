import sys, os
from winreg import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QCoreApplication

def appver():
    return "0.1"

class MyApp(QMainWindow):
    def addRegistry(self):
        sdp_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
        key = CreateKey(HKEY_LOCAL_MACHINE, sdp_path)
        try:
            SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x0)
            self.statusBar().showMessage(" Installed WinWD. (Add on Windows Registry.)")
        except EnvironmentError:
            self.envError()

    def check(self):
        sdp_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, sdp_path, 0, KEY_ALL_ACCESS)
        except OSError:
            return None
        return key

    def de(self):
        key = self.check()
        if key is not None:
            return True
        else:
            return False

    def act(self, i):
        key = self.check()
        if key is not None:
            v = EnumValue(key, 0)
            if v[1] == i:
                return False
            else:
                return True
        if key is None:
            return False

    def writeDisable(self):
        key = self.check()
        if key is None:
            self.statusBar().showMessage(" You need installed WinWB first. Please select 'Install WinWB GUI' and retry.")
        else:
            try:
                SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x1)
                self.statusBar().showMessage(" Write blocking on. (Write is disabled now.)")
            except EnvironmentError:
                self.envError()

    def writeAble(self):
        key = self.check()
        if key is None:
            self.statusBar().showMessage(" You need installed WinWB first. Please select 'Install WinWB GUI' and retry.")
        else:
            try:
                SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x0)
                self.statusBar().showMessage(" Write blocking off. (Write is able now.)")
            except EnvironmentError:
                self.envError()

    def deleteRegistry(self):
        sdp_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
        try:
            DeleteKey(HKEY_LOCAL_MACHINE, sdp_path)
            self.statusBar().showMessage(" Removed WinWB. (Deleted on Windows Registry.)")
        except FileNotFoundError:
            self.statusBar().showMessage(" You need installed WinWB first. Please select 'Install WinWB GUI' and retry.")

    def envError(self):
        self.statusBar().showMessage(" Encountered Environment Error")

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        def dis():
            btn1.setEnabled(self.act(1))
            btn2.setEnabled(self.act(0))
            btn3.setEnabled(not self.de())
            btn4.setEnabled(self.de())
        def on():
            self.writeDisable()
            dis()
        def off():
            self.writeAble()
            dis()
        def re():
            self.addRegistry()
            dis()
        def dele():
            self.deleteRegistry()
            dis()

        # Label
        mainlogo = QLabel(self)
        pixmap = QPixmap(os.path.join(pwdir, "images", "logo-main.png"))
        mainlogo.setPixmap(pixmap)
        self.setCentralWidget(mainlogo)
        self.resize(pixmap.width(), pixmap.height())
        # Button
        btn1 = QPushButton(" Write Blocker On ", self)
        btn1.setGeometry(400, 30, 150, 30)
        btn1.setEnabled(self.act(1))
        btn1.clicked.connect(on)
        btn2 = QPushButton("Write Blocker Off", self)
        btn2.setGeometry(400, 70, 150, 30)
        btn2.setEnabled(self.act(0))
        btn2.clicked.connect(off)
        btn3 = QPushButton("Install WinWB GUI", self)
        btn3.setGeometry(400, 110, 150, 30)
        btn3.setEnabled(not self.de())
        btn3.clicked.connect(re)
        btn4 = QPushButton("Remove WinWB GUI", self)
        btn4.setGeometry(400, 150, 150, 30)
        btn4.setEnabled(self.de())
        btn4.clicked.connect(dele)
        btn0 = QPushButton("Quit", self)
        btn0.move(470, 210)
        btn0.resize(btn0.sizeHint())
        btn0.clicked.connect(QCoreApplication.instance().quit)
        # Interface
        self.statusBar().showMessage("Version: " + appver())
        self.setWindowIcon(QIcon(os.path.join(pwdir, "images", "logo.ico")))
        self.setWindowTitle(" WinWB GUI")
        self.move(320, 320)
        self.setFixedSize(580, 280)
        self.show()

pwdir = os.path.dirname(__file__)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MyApp()
    sys.exit(app.exec())
