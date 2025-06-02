import os
import time

def get_uptime():
    if os.name == "posix":
        # Linux/Unix systems
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.readline().split()[0])
    elif os.name == "nt":
        # Windows systems
        import ctypes
        import sys
        if sys.getwindowsversion().major >= 6:
            # Windows Vista or later
            kernel32 = ctypes.windll.kernel32
            uptime_ms = kernel32.GetTickCount64()
        else:
            uptime_ms = ctypes.windll.kernel32.GetTickCount()
        uptime_seconds = uptime_ms / 1000.0
    else:
        raise NotImplementedError("Unsupported OS")

    return uptime_seconds

def format_uptime(seconds):
    mins, secs = divmod(int(seconds), 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    return f"{days}d {hours}h {mins}m {secs}s"

if __name__ == "__main__":
    uptime_seconds = get_uptime()
    print("System Uptime:", format_uptime(uptime_seconds))
