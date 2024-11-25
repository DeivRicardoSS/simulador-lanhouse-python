import os
import platform

def clear():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")
