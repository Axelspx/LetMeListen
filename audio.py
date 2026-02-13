from pycaw.pycaw import AudioUtilities
import win32process
import win32gui

muted = False

#TODO: Pass all sessions to mute_session_toggle, to mute all except foreground(pid) session

def mute_session_toggle(pid, sessions):
    global muted

    for session in sessions:
        if session.Process and session.Process.pid != pid:
            if not muted:
                print(f"Muting background process:{session.Process.pid}")
                session.SimpleAudioVolume.SetMute(1, None)
            if muted:
                print(f"Unmuting background process: {session.Process.pid}")
                session.SimpleAudioVolume.SetMute(0, None)

        #if session.Process and session.Process.pid == pid:
            #session.SimpleAudioVolume.SetMute(0, None)