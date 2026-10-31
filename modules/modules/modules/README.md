Linux Privilege Escalation Automation Toolkit

Project Overview

The Linux Privilege Escalation Automation Toolkit is a Python-based security auditing tool designed to identify potential Linux system misconfigurations and permission-related security risks.

Objectives

- Collect Linux system information.
- Check important file permissions.
- Review sudo permission information.
- Generate security audit reports.
- Help security learners understand Linux security configurations.

Features

1. System Information Collection
2. Permission Auditing
3. Sudo Configuration Review
4. Security Report Generation

Technologies Used

- Python 3
- Linux
- Kali Linux
- GitHub

Project Structure

Linux-Privilege-Escalation-Toolkit/
├── main.py
├── README.md
├── requirements.txt
├── modules/
│   ├── system_info.py
│   ├── permission_checks.py
│   └── security_report.py
└── reports/
    └── .gitkeep

Installation

Clone the repository:

git clone YOUR_REPOSITORY_URL

Open the project:

cd Linux-Privilege-Escalation-Toolkit

Run:

python3 main.py

Disclaimer

This toolkit is intended for educational purposes and authorized security auditing only. It does not perform automatic exploitation.
