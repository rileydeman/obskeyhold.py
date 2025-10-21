# --- Imports ---
import importlib.util, subprocess, sys
from config.variables import *

# --- Variables ---
checkedForPackages = int(0)
packages = [
    {
        "name": "keyboard",
        "installed": bool(False)
    }
]

# --- Package Checker function ---
def checkPackages():
    if OS != "Windows":
        sys.exit(f"Unsupported operating system detected ({OS}).\n> Package installation skipped\n{LINE}")

    global checkedForPackages, packages
    reRunFunction = bool(False)

    print("Checking packages...\n")

    for pkg in packages:
        if checkedForPackages == 0 or not pkg["installed"]:
            spec = importlib.util.find_spec(pkg["name"])

            if spec is None:
                print(f"{pkg['name']} is not installed! Installing...")
                reRunFunction = True

                subprocess.check_call([sys.executable, "-m", "pip", "install", pkg["name"]])
            else:
                pkg["installed"] = True

                if checkedForPackages == 0:
                    print(f"{pkg['name']} is already installed!")
                else:
                    print(f"{pkg['name']} is installed!")

    checkedForPackages += 1
    if reRunFunction:
        print("Re-running packages check...")

        if checkedForPackages < 5:
            checkPackages()
    else:
        print(f"All packages are available!\n{LINE}")