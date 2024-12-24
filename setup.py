import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["pygame"],
    "include_files": []
}

# GUI applications require a different base on Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Tetris",
    version="1.0",
    description="Tetris Game",
    options={"build_exe": build_exe_options},
    executables=[Executable("tetris.py", base=base, icon="icon.ico")]
)