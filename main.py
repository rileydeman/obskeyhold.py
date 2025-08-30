# packages Check
from config.packages import checkPackages
checkPackages()


# Imports
import time
import keyboard
from config.variables import *

# Functions
def nowMS():
    return time.time() * 1000

def checkValidInput(inp, type):
    for key in KEYS:
        if key["input"] == inp:
            isShown = bool(False)
            wasPressed = key["wasPressed"]

            if type == "KD":
                key["wasPressed"] = True
                execute = bool(False)
                downSince = nowMS()

                while not execute and not isShown:
                    if (nowMS() - downSince) >= key["delay"]:
                        execute = True

                if execute:
                    keyboard.send(key["show"])
                    isShown = True

            elif type == "KU":
                if wasPressed:
                    keyboard.send(key["hide"])


print("Helper running. Press esc in this window to stop.")
print("Listening for:\n")

for key in KEYS:
    print(f"{key["input"]}: {key['name']}")

print(LINE)

while runProgram:
    e = keyboard.read_event()
    key = e.name

    if e.event_type == keyboard.KEY_DOWN:

        print(f"Key down: {key}")

        checkValidInput(key, "KD")

        if key == "esc":
            runProgram = False

    if e.event_type == keyboard.KEY_UP:
        print(f"Key released: {key}")
        checkValidInput(key, "KU")