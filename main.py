# --- Operating System Check ---
from config.os import checkOS
checkOS()

# --- Packages Check ---
from config.packages import checkPackages
checkPackages()

# --- Imports ---
import keyboard, platform, signal, time
from config.variables import *

# --- Disable Ctrl+C ---
signal.signal(signal.SIGINT, signal.SIG_IGN)

# --- Functions ---
def nowMS():
    return time.time() * 1000.0

def checkValidInput(inp, type):
    for key in KEYS:
        if key["input"] == inp:
            wasPressed = key["wasPressed"]

            if type == "KD" and not wasPressed:
                key["wasPressed"] = True

                if key.get("delay", 0) == 0:
                    keyboard.press(key["show"])
                    time.sleep(0.05)
                    keyboard.release(key["show"])
                    key["shown"] = True
                    print(f"{key['name']}: is now active")

            elif type == "KU" and wasPressed:
                keyboard.press(key["hide"])
                time.sleep(0.05)
                keyboard.release(key["hide"])
                key["wasPressed"] = False
                key["shown"] = False
                print(f"{key['name']}: is now not active")

# --- Main Program ---
print("Helper running. Press ctrl+esc or ctrl+c in this window to stop.")
print("Listening for:")

for key in KEYS:
    print(f"{key["input"]}: {key["name"]}")

print(LINE)

while runProgram:
    if (keyboard.is_pressed("ctrl") and keyboard.is_pressed("esc")) or (keyboard.is_pressed("ctrl") and keyboard.is_pressed("c")):
        runProgram = False
        print(f"Ending program...\n{LINE}")
        break

    for key in KEYS:
        down = keyboard.is_pressed(key["input"])

        if down and not key["wasPressed"]:
            checkValidInput(key["input"], "KD")

        if not down and key["wasPressed"]:
            checkValidInput(key["input"], "KU")

    time.sleep(PROGRAM_COOLDOWN)
