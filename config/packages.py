import importlib.util
import subprocess
import sys
from config.variables import *

checkedForPackages = int(0)
packages = [
    {
        "name": "keyboard",
        "installed": bool(False)
    }
]

def checkPackages():
    global checkedForPackages, packages
    reRunFunction = bool(False)

    print("Checking packages...")

    for pkg in packages:
        if checkedForPackages == 0 or not pkg["installed"]:
            spec = importlib.util.find_spec(pkg["name"])

            if spec is None:
                print(f"{pkg["name"]} is not installed! Installing...")
                reRunFunction = True

                subprocess.check_call([sys.executable, "-m", "pip", "install", pkg["name"]])
            else:
                pkg["installed"] = True

                if checkedForPackages == 0:
                    print(f"{pkg["name"]} is already installed!")
                else:
                    print(f"{pkg["name"]} is installed!")

    checkedForPackages += 1
    if reRunFunction:
        print("Re-running packages check...")

        if checkedForPackages < 5:
            checkPackages()
    else:
        print(f"All packages are available!\n{LINE}")