import sys
from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY'] = "C:\\Anaconda\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Anaconda\\tcl\\tk8.6"

setup(

    name = "Snake",
    version = "1.1",
    description = "fun.",
    executables = [Executable("D:\Python\Snake.py", base = "Win32GUI")])
