from datetime import datetime
import os

def generate_report(results):

os.makedirs("reports", exist_ok=True)

filename = "reports/security_audit_report.txt"

with open(filename, "w") as report:

    report.write("LINUX SECURITY AUDIT REPORT\n")
    report.write("=" * 40 + "\n")

    report.write(
        "Date: " + datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ) + "\n\n"
    )

    for item in results:
        report.write(str(item) + "\n")

    report.write("\nAudit completed successfully.\n")

print("\nReport saved:", filename)

if name == "main":
generate_report([
"System information checked",
"Permission audit completed",
"Security review completed"
])
