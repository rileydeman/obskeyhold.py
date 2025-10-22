# --- Imports ---
import sys
from config.variables import OS, LINE

# --- OS check function ---
def checkOS():
    if OS == "Windows":
        print(f"Supported operating system detected ({OS}).\n{LINE}")
    else:
        print(f"Unsupported operating system detected ({OS}).\n> This program only accepts Windows!\n{LINE}")
        sys.exit(1)