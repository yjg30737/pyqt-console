# pyqt-console
PyQt console which ansi2html package is applied, colorful, console-like output like cmd, bash, etc.

The console widget (with the class name 'ConsoleWidget') inherits from QTextBrowser and extracts the results of specific commands in this QTextBrowser.

This will be used a lot for PyQt-AI related applications, so i want to share this with you :)

You have to check each `ConsoleThread` class in pyqt_console_thread.py and `ConsoleWidget` class in pyqt_console.py to know how this works, if you want to use it :)

## Reqirements
* PyQt5 >= 5.14
* ansi2html

## How to
1. git clone ~
2. pip install -r requirements.txt
3. python main.py

## Preview
![image](https://github.com/yjg30737/pyqt-console/assets/55078043/cc69a6f3-b5f6-4924-b74f-b9b96c15394e)
