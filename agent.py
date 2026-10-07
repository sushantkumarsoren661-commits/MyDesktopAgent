import keyboard
import time 
import win32gui
from pywinauto import Desktop

def trigger_assistant():
    print("\n[+] Hotkey Detected! Assistant waking up...")

    time.sleep(0.5)

    try:
        hwnd = win32gui.GetForegroundWindow()

        active_window = Desktop(backend = "uia").window(handle = hwnd)
        window_title = active_window.window_text()

        print(f"[+] Active window dected {window_title}")

        command = input("\n What would you like me to do ? > ")
        print(f"[+] Received command: '{command}' for window: '{window_title}'")

        # --- THE HANDS (EXECUTION) ---
        # Check if the command starts with the word "type "

        if command.lower().startswith("type "):
            text_to_type = command[5:] # Grab everything after the word "type "
            print(f"[*] Executing: Typing '{text_to_type}' into the active window...")
            
            # Send the keystrokes to the active window
            active_window.type_keys(text_to_type, with_spaces=True)
            print("[+] Action complete!")
        else:
            print("[-] I only know how to 'type' things right now! Try a command like: type hello world")

    except Exception as e:
        print(fr"[-] Error reading window: {e}")

print("Desktop Agent is running  in the background...")
print("Press 'Ctrl + Windows' to trigger it. Press Esc to quit.")

keyboard.add_hotkey('ctrl + windows', trigger_assistant)
keyboard.wait('esc')
