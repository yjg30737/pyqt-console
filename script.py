import os

platform = os.sys.platform

if platform == "win32":
    os.system("ipconfig")
elif platform == "linux" or platform == "linux2":
    os.system("ifconfig")
elif platform == "darwin":  # 맥 OS
    os.system("ifconfig")
else:
    print("OS not supported")
