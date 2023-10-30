import os, sys

from pyqt_console_thread import ConsoleThread

# Get the absolute path of the current script file
script_path = os.path.abspath(__file__)

# Get the root directory by going up one level from the script directory
project_root = os.path.dirname(os.path.dirname(script_path))

sys.path.insert(0, project_root)
sys.path.insert(0, os.getcwd())  # Add the current directory as well

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QCoreApplication

from pyqt_console import ConsoleWidget

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support

QApplication.setFont(QFont('Arial', 12))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('PyQt console example')
        btn = QPushButton()
        btn.setText('Run!')
        btn.clicked.connect(self.__run)
        self.__consoleWidget = ConsoleWidget()

        lay = QVBoxLayout()
        lay.addWidget(btn)
        lay.addWidget(self.__consoleWidget)
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)

    def __run(self):
        self.__t = ConsoleThread()
        self.__t.started.connect(self.__started)
        self.__t.updated.connect(self.__consoleWidget.append)
        self.__t.finished.connect(self.__finished)
        self.__t.start()

    def __started(self):
        self.__consoleWidget.append('Started')

    def __finished(self):
        self.__consoleWidget.append('Finished')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())