# Lab 11: Automating Software Packages with Ansible

## Overview
This repository contains complete enterprise playbooks for automated software package lifecycle management across multi-OS Linux architectures (CentOS/RHEL and Ubuntu).

## Architecture & Implementation Highlights
- **Cross-Platform Abstraction:** Generic package mapping using `package`, `yum`, and `apt` modules.
- **Repository Provisioning:** Automated injection of Third-Party EPEL and Docker CE repositories with GPG verification.
- **Resilient Error Handling:** `block-rescue` constructs that isolate optional package failures from breaking critical workflow executions.
- **Audit & Analytics:** Automated state snapshots (`rpm -qa`, `dpkg -l`) and centralized report generation on the Ansible control node.

## Playbook Catalog
1. `playbooks/install-basic-packages.yml` - Foundation packages deployment and version assertion.
2. `playbooks/advanced-package-management.yml` - Language toolchain installation and legacy package removal.
3. `playbooks/rhel-package-management.yml` - RedHat ecosystem updates, EPEL, and Docker CE repo configurations.
4. `playbooks/ubuntu-package-management.yml` - Apt cache updates, dist-upgrade, Docker repos, and PyPI integration.
5. `playbooks/universal-package-management.yml` - Unified web server, MariaDB, and Nagios deployment stack.
6. `playbooks/robust-package-management.yml` - Failure-tolerant execution with backup logging.
7. `playbooks/package-reporting.yml` - System audit engine generating text dashboards under `/tmp/ansible_reports/`.
