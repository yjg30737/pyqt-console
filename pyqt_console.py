from PyQt5.QtWidgets import QWidget, QTextBrowser
from ansi2html import Ansi2HTMLConverter


class ConsoleWidget(QTextBrowser):
    def __init__(self):
        super(QWidget, self).__init__()
        self.__conv = Ansi2HTMLConverter()
        self.__initUi()

    def __initUi(self):
        self.setStyleSheet('QTextBrowser { background-color: #333; }')
        # you can change the font like below
        # font = QFont("Courier", 10)
        # self.setFont(font)

    def append(self, text: str) -> None:
        super(ConsoleWidget, self).append(self.__conv.convert(text.strip()))