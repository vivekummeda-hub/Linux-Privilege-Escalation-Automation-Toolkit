import os
import platform
import subprocess

print("=" * 50)
print(" LINUX PRIVILEGE ESCALATION AUDIT TOOLKIT")
print("=" * 50)

print("\n[1] SYSTEM INFORMATION")

print("Operating System:", platform.system())
print("Hostname:", platform.node())
print("Kernel:", platform.release())
print("Architecture:", platform.machine())

print("\n[2] CURRENT USER")

try:
    user = subprocess.check_output(
        ["whoami"], text=True
    ).strip()
    print("Current User:", user)
except Exception:
    print("User information unavailable")

print("\n[3] SUDO PERMISSIONS")

try:
    result = subprocess.run(
        ["sudo", "-n", "-l"],
        capture_output=True,
        text=True,
        timeout=5
    )
    print(result.stdout or "No sudo permissions displayed")
except Exception:
    print("Sudo check unavailable")

print("\n[4] SECURITY AUDIT")

paths = ["/etc/passwd", "/etc/shadow", "/etc/sudoers"]

for path in paths:
    if os.path.exists(path):
        print(path, "EXISTS")

print("\n[5] AUDIT COMPLETED")
print("=" * 50)
