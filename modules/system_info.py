import platform
import subprocess

def get_system_info():
print("\n===== SYSTEM INFORMATION =====")

print("Operating System:", platform.system())
print("Hostname:", platform.node())
print("Kernel Version:", platform.release())
print("Architecture:", platform.machine())

try:
    uptime = subprocess.check_output(
        ["uptime", "-p"],
        text=True
    ).strip()

    print("System Uptime:", uptime)

except Exception:
    print("Uptime information unavailable")

if name == "main":
get_system_info()
