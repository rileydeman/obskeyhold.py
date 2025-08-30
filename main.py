# packages Check
from config.packages import checkPackages
checkPackages()

# Imports
import time
import keyboard
from config.variables import *

# Functions
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

            elif type == "KU" and wasPressed:
                keyboard.press(key["hide"])
                time.sleep(0.05)
                keyboard.release(key["hide"])
                key["wasPressed"] = False
                key["shown"] = False

# Main Program
print("Helper running. Press esc in this window to stop.")
print("Listening for:\n")

for key in KEYS:
    print(f"{key["input"]}: {key["name"]}")

print(LINE)

while runProgram:
    if keyboard.is_pressed("esc"):
        runProgram = False
        break

    for key in KEYS:
        down = keyboard.is_pressed(key["input"])

        if down and not key["wasPressed"]:
            checkValidInput(key["input"], "KD")

        if not down and key["wasPressed"]:
            checkValidInput(key["input"], "KU")


    time.sleep(PROGRAM_COOLDOWN)
