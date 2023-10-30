import subprocess

from PyQt5.QtCore import QThread, pyqtSignal


class ConsoleThread(QThread):
    updated = pyqtSignal(str)

    def __init__(self, **common_args):
        super(ConsoleThread, self).__init__()
        self.__common_args = common_args

    def run(self):
        try:
            command = 'python script.py'

            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                errors='replace'
            )

            while True:
                realtime_output = process.stdout.readline()
                if realtime_output == '' and process.poll() is not None:
                    print('Thread end for a variant of reasons')
                    break
                if realtime_output:
                    self.updated.emit(realtime_output)
        except Exception as e:
            print('Error')
            raise Exception(e)