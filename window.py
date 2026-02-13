import win32
import win32process
import win32gui

#TODO: Get pids of all background sessions to pass to audio.py

def get_foreground() -> tuple:
    # gets foreground window HWND, then gets thread and process identifier of window origin process
    hwnd = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(hwnd) #thread identifier(_) not needed
    print(f" - HWND: {hwnd} \n - PID: {pid}")
    return hwnd, pid





if __name__ == "__main__":
    print(get_foreground())