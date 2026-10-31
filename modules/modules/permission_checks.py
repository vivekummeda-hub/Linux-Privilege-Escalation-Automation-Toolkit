import os
import stat

def check_permissions():

print("\n===== PERMISSION AUDIT =====")

paths = [
    "/etc/passwd",
    "/etc/shadow",
    "/etc/sudoers",
    "/tmp"
]

for path in paths:

    if os.path.exists(path):

        permissions = stat.filemode(
            os.stat(path).st_mode
        )

        print(f"{path}: {permissions}")

    else:
        print(f"{path}: Not found")

if name == "main":
check_permissions()
