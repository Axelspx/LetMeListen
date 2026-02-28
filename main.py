from pycaw.pycaw import AudioUtilities
import win32process
import win32gui
import keyboard
import time
import comtypes
from typing import Any
import psutil

comtypes.CoInitialize()

mute_hotkey: list= ["alt", "x"]
muted: bool= False

## MAIN APP CONTROL ##

def toggle_mute():
    global muted
    print(f"Keyboard hotkey pressed")
    mute_sessions_toggle()
    muted = not muted
    return



## WINDOW ##

def get_foreground() -> list:
    # gets foreground window HWND, then gets thread and process identifier of window origin process
    fg_hwnd = win32gui.GetForegroundWindow()
    _, fg_pid = win32process.GetWindowThreadProcessId(fg_hwnd) #thread identifier(_) not needed
    child_pids = get_foreground_children(fg_pid)
    fg_title = win32gui.GetWindowText(fg_hwnd)
    print(f" - Foreground window:\n   {fg_title}\n - Relevant PIDs:\n   {[fg_pid]+child_pids}")
    return [fg_pid] + child_pids

def get_foreground_children(fg_pid):
    try:
        process = psutil.Process(fg_pid)
        children = process.children(recursive=True) #recursive gets all descendants of process; children, grandchildren etc
        return [child.pid for child in children]
    except Exception:
        return []



## AUDIO ##

def get_audio_sessions() -> list:
    comtypes.CoInitialize()
    sessions = AudioUtilities.GetAllSessions()
    return sessions

def mute_sessions_toggle() -> Any:
    pids = get_foreground()
    sessions = get_audio_sessions()
    for session in sessions:
        if not muted and session.Process and session.Process.pid not in pids:
            print(f"Muting background process - PID:{session.Process.pid}")
            session.SimpleAudioVolume.SetMute(1, None)
        if muted and session.Process:
            print(f"Unmuting background process: {session.Process.pid}")
            session.SimpleAudioVolume.SetMute(0, None)




if __name__ == "__main__":
    keyboard.add_hotkey("+".join(mute_hotkey), toggle_mute)
    while True:
        time.sleep(0.1)