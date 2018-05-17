import sys
from cx_freeze import setup, Executable

setup(
    name="snakeface",
    version="1.1",
    description="A snake game",
    executables=[Executable("snakeface.py",base="Win64GUI")])
