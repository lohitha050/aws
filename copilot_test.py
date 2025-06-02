import os
import platform
import subprocess

def get_uptime():
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        try:
            # Use the 'uptime' command
            output = subprocess.check_output("uptime -p", shell=True, text=True)
            print("System Uptime:", output.strip())
        except Exception as e:
            print("Error getting uptime:", e)
    elif system == "Windows":
        try:
            # Use 'net stats srv' and parse output
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("System Uptime (since):", line)
                    break
        except Exception as e:
            print("Error getting uptime:", e)
    else:
        print("Unsupported Operating System")

if __name__ == "__main__":
    get_uptime()
