from cx_Freeze import setup, Executable


exe = Executable(
    script="test1.py",
    base="Win32GUI"
)


setup(
    name="wxSampleApp",
    version="0.1",
    description="example",
    executables=[Executable("test1.py")]
)