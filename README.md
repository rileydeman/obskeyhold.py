# obskeyhold.py

![Built with Python](https://img.shields.io/badge/built_with-Python-blue?logo=python)
![Python Version](https://img.shields.io/badge/python-3.14%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-blue?logo=windows)
![Architecture](https://img.shields.io/badge/architecture-x64-lightblue)
![Version](https://img.shields.io/badge/version-1.0.0-success)
![License](https://img.shields.io/badge/license-Custom-lightgrey)
![Status](https://img.shields.io/badge/status-Stable-brightgreen)
![Contributions](https://img.shields.io/badge/contributions-closed-red)


A small, lightweight **OBS Studio helper** written in Python.  
This tool allows streamers to automatically hide or show in-game maps (like in *Rust*) while holding specific keys — keeping private locations secret from viewers while still allowing smooth gameplay.

--- 

## 📚 Table of Contents

- [Overview](#-overview)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technical Information](#-technical-information)
- [License Notice](#-license-notice)
- [Copyright](#-copyright)
- [License](#-license)

---

## 🧩 Overview

`obskeyhold.py` is a **Windows-only helper tool** designed for streamers who use **OBS Studio** while playing games such as *Rust*, *DayZ*, or other open-world titles where showing the in-game map could reveal their position to viewers.

When you hold down certain keys in-game, OBS can automatically toggle overlays or sources (like hiding a map capture).  
This script automates that key press/release behavior, using Python to send **virtual key events (F13–F24)** — keys that OBS can detect as hotkeys without interfering with your normal gameplay.

**Core Features**
- 🎮 Hold-to-toggle behavior for hiding in-game maps.
- 🧠 Lightweight and simple to run — no setup tools or extra dependencies required.
- 🪟 Designed specifically for **Windows 10/11 (x64)**.
- ⚙️ Easy customization through the `config/variables.py` file.

**Use case example**
> You hold `G` to open your in-game map — OBS automatically hides your map overlay so viewers can’t see your location. When you release `G`, the map reappears in your stream.


---

## ⚙️ Installation

Follow these steps to install and run **obskeyhold.py**:

1. **Download the latest release**
   - Go to the [Releases](https://github.com/rileydeman/obskeyhold.py/releases) page.
   - Under **Assets**, download the file named **Source code (zip)**.
   - This will download a file such as `obskeyhold.py-1.0.0.zip`.

2. **Extract the files**
   - Right-click the ZIP file → **Extract All...**
   - Choose a simple folder path, for example:  
     `C:\obskeyhold`

3. **Open Command Prompt in that folder**
   - Open the folder where you extracted the project.  
   - Click on the **address bar** in File Explorer (the path at the top).  
   - Type `cmd` and press **Enter** — this will open Command Prompt directly in that folder.

4. **Run the program**
   Depending on your Python setup, one of these commands will start the program: \
    Option 1 (most common)
   ```bash
   main.py
   ```
   Option 2:
    ```bash
   python main.py
    ```
   Option 3:
    ```bash
   py main.py
    ```
5. **(First run only)**  
   - When you start the program for the first time, it automatically checks for required Python packages (like `keyboard`).
   - If something is missing, it installs it automatically.
   - Once the setup is complete, the program re-runs automatically and begins listening for key input.

6. **Done!**  
   The helper is now active and ready to use together with your configured OBS Studio hotkeys.  
   You’ll see a message similar to:
    ```
   Helper running. Press ctrl+esc or ctrl+c in this window to stop.
   Listening for:
   g: NoLookie Map 
   
   =========================================
   ```

---

## 💻 Usage

1. **Keep the console window open**  
   The script must stay running while you stream.  
   You can minimize the console window, but do not close it — if the program isn’t running, your OBS hotkeys won’t respond.

2. **About the F13–F24 keys**
   - Most keyboards physically stop at **F12**, but Windows internally supports keys **F13** through **F24**.
   - These keys are “virtual” — you can’t press them yourself, but this program can send them.
   - OBS can detect these virtual keys as hotkeys, which makes them perfect for automating map hiding and other actions.
   - ⚠️ **Important:** The helper must be **running** while you configure OBS hotkeys.  
     If it isn’t running, OBS will not detect the virtual keys.

3. **Configure OBS hotkeys**
   - Open **OBS Studio → Settings → Hotkeys**.  
   - Make sure the helper program is already running in the background.
   - When OBS asks you to set a hotkey:
     - To set **F13** (the “show” action): **hold your in-game key** (for example `G`).
     - To set **F14** (the “hide” action): **release that same key**.
   - The helper will send the correct virtual keys to OBS while you press and release your chosen key.  
     OBS will then register them as `F13` and `F14`.

4. **Default behavior**
   - When you press your configured key (for example `G`), the script sends the assigned **“show”** key (e.g. `F13`) to OBS.  
   - When you release the key, it sends the **“hide”** key (e.g. `F14`).
   - This allows OBS to toggle overlays, maps, or other sources automatically.

5. **Customize key mappings**
   - Open `config/variables.py` in a text editor.  
   - Modify or add entries in the `KEYS` list:
     ```python
     KEYS = [
         {
             "name": "NoLookie Map Cover",
             "input": "g",
             "show": "f13",
             "hide": "f14",
             "delay": 0
         }
     ]
     ```
   - Save the file and restart the program to apply your changes.

6. **Stop the helper**
   - Click the console window to make sure it’s focused.  
   - Press **Ctrl + Esc** or **Ctrl + C** to safely stop the program.

The tool will now handle your key presses automatically while you stream, ensuring your viewers can’t see sensitive in-game map information.


---

## 🧠 Technical Information

<table>
<thead>
    <tr>
        <th>Specification</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Programming Languages</td>
        <td>Python</td>
    </tr>
    <tr>
        <td>Packages Used</td>
        <td>keyboard</td>
    </tr>
    <tr>
        <td>APIs Used</td>
        <td>None</td>
    </tr>
    <tr>
        <td>Deployment Target</td>
        <td>Windows</td>
    </tr>
    <tr>
        <td>Primary Language</td>
        <td>English (en-AU)</td>
    </tr>
</tbody>
</table>

---

## 🧩 Troubleshooting

Having issues getting **obskeyhold.py** to work correctly?  
Here are some common problems and their solutions:

### 🔹 OBS doesn’t detect the key when assigning F13–F24
- Make sure **obskeyhold.py is running** before you open the OBS **Hotkeys** settings.  
- While setting a hotkey in OBS:
  - **Hold your configured key** (for example `G`) to set **F13**.
  - **Release it** to set **F14**.
- If OBS still doesn’t detect the input, restart both **OBS Studio** and **obskeyhold.py**, then try again.

### 🔹 Nothing happens when pressing the key in-game
- Check that the console window says something like:
    ```
    Listening for:
    g: NoLookie Map Cover
    ```
- If it doesn’t show your key name, verify that the `input` value in `config/variables.py` matches the key you’re pressing (for example `"g"`).  
- Make sure the console window remains **open** and that the program is still running.  
- If you modified the config file, **save it** and then **restart the program**.

### 🔹 The program closes instantly
- This usually happens if **Python** isn’t installed or isn’t added to your system PATH.  
- Check by running python --version` or `py --version` in Command Prompt.  
- If it says the command isn’t recognized, [download Python](https://www.python.org/downloads/windows/) and check **“Add Python to PATH”** during installation.
- You can also start the script manually to see any error messages:
```bash
  python main.py
```

### 🔹 OBS hotkeys trigger the wrong source
- Double-check your hotkey setup in **OBS → Settings → Hotkeys**:  
  - Each **Show Source** action should match your configured `show` key (for example `F13`).  
  - Each **Hide Source** action should match your `hide` key (for example `F14`).
- Avoid assigning the same F-key pair (like F13/F14) to multiple sources unless that behavior is intentional.

### 🔹 Still not working?
If you’ve verified all steps above and the tool still doesn’t respond:
1. Close both **OBS Studio** and **obskeyhold.py**.  
2. Reopen **OBS** first.  
3. Then run **obskeyhold.py** again.  
4. Try pressing your configured key.

If the issue continues, re-download the latest version from the [Releases](https://github.com/rileydeman/obskeyhold.py/releases) page to ensure you’re running the newest build.


---

## ⚠️ License Notice

This project is licensed for **personal and educational use only**.

- ✅ **Allowed:** Personal projects, private learning, classroom demonstrations, and student research.
- ❌ **Not allowed:** Public sharing, republishing, redistribution, or any form of commercial use.

To use this project (or any part of it) in a **public** or **commercial** context, you must obtain **written permission** from the author:

**Author:** [@rileydeman](https://github.com/rileydeman)

See the full [LICENSE](./LICENSE) file for complete terms and conditions.

---

## ©️ Copyright

All code and visual assets in this repository are &copy; rileydeman.

- Code is licensed for personal and educational use only.
- Logos, icons, and images are not open source and may not be reused without permission.

See the [LICENSE](./LICENSE) file for full terms.

---

## 📝 License

Custom license &copy; [rileydeman](https://github.com/rileydeman)  
See the [LICENSE](./LICENSE) file for full terms.

---

&copy; [rileydeman](https://www.rileydeman.com/)