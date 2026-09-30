import keyboard
import time 
import win32gui
from pywinauto import Desktop

def trigger_assistant():
    print("\n[+] Hotekey Detected! Assistant waking up...")

    time.sleep(0.5)

    try:
        hwnd = win32gui.GetForegroundWindow()

        active_window = Desktop(backend = "uia").window(handle = hwnd)
        window_title = active_window.window_text()

        print(f"[+] Active window dected {window_title}")

        command = input("\n What would you like me to do ? > ")
        print(f"[+] Received command: '{command}' for window: '{window_title}'")

    except Exception as e:
        print(fr"[-] Error reading window: {e}")

print("Desktop Agent is running  in the background...")
print("Press 'Ctrl + Windows' to trigger it. Press Esc to quit.")

keyboard.add_hotkey('ctrl + windows', trigger_assistant)
keyboard.wait('esc')
