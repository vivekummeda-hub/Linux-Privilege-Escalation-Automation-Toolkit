from modules.system_info import get_system_info
from modules.permission_checks import check_permissions
from modules.security_report import generate_report

def main():

    print("=" * 50)
    print(" LINUX PRIVILEGE ESCALATION AUTOMATION TOOLKIT")
    print("=" * 50)

    print("\n[1] SYSTEM INFORMATION")
    get_system_info()

    print("\n[2] PERMISSION AUDIT")
    check_permissions()

    print("\n[3] SECURITY REPORT")

    results = [
        "System information checked",
        "File permissions audited",
        "Security review completed"
    ]

    generate_report(results)

    print("\nAUDIT COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    main()
