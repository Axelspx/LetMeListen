#import pycaw
#import win32
#import win32process
#import win32gui
import keyboard
import time

from audio import mute_session_toggle
from window import get_foreground
from hotkey import mute_hotkey

def mute_focus_window():
    print(f"Keyboard hotkey pressed")
    mute_session_toggle(get_foreground())
    return

#def keyboard_hook(event):
    #print(event.name)


if __name__ == "__main__":

    #keyboard.hook(keyboard_hook)
    keyboard.add_hotkey("+".join(mute_hotkey), mute_focus_window)

    while True:
        time.sleep(0.1)