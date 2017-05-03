import sys


os = sys.platform

if os == "win32":
    pass
elif os.startswith("linux"):
    import subprocess
    subprocess.Popen(['ls'])