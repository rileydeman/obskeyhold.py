# --- Imports ---
import platform

# --- Constants ---
LINE = "\n=========================================\n"
PROGRAM_COOLDOWN = 0.01
OS = platform.system()
KEYS = [
    {
        "name": "NoLookie Map Cover",
        "input": "g",
        "wasPressed": False,
        "show": "f13",
        "hide": "f14",
        "delay": 0  # Require key to be held this miliseconds long before SHOW (0 = immediate)
    },
    # Add more keys if you want
]

# --- Variables ---
runProgram = bool(True)