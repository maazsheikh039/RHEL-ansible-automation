# Ansible Infrastructure as Code (IaC) & Automation Labs - Master Repository

[![Ansible Core](https://img.shields.io/badge/Ansible-2.14+-EE0000?style=for-the-badge&logo=ansible&logoColor=white)](https://www.ansible.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![IaC Status](https://img.shields.io/badge/IaC-Production--Ready-success?style=for-the-badge&logo=terraform&logoColor=white)](https://github.com/)
[![Security](https://img.shields.io/badge/Security-AES256%20Vault-red?style=for-the-badge&logo=1password&logoColor=white)](https://docs.ansible.com/ansible/latest/vault_guide/index.html)

Welcome to the **Ansible Infrastructure as Code (IaC) & Automation Labs** master repository. This repository represents a complete, production-grade automation curriculum and enterprise portfolio. It spans **20 hands-on labs** covering Linux system administration, security hardening, database provisioning, multi-tier application orchestration, secrets management with Ansible Vault, fault-tolerant error handling, and performance optimization.

Designed according to Red Hat Enterprise Linux (RHEL) Automation standards and Red Hat Ansible Automation Platform (AAP) best practices, this repository serves as both a comprehensive learning path and an production-grade reference architecture for DevOps and Automation Engineers.

---

## 📋 Table of Contents

- [Architectural Overview & Core Capabilities](#-architectural-overview--core-capabilities)
- [Comprehensive Lab Index (Labs 01 - 20)](#-comprehensive-lab-index-labs-01---20)
- [Repository Directory Structure](#-repository-directory-structure)
- [Prerequisites & Environment Setup](#-prerequisites--environment-setup)
- [How to Run & Verify Labs](#-how-to-run--verify-labs)
- [Key Enterprise Features](#-key-enterprise-features)
- [License & Verification](#-license--verification)

---

## 🏗 Architectural Overview & Core Capabilities

This repository demonstrates end-to-end automation capability across enterprise IT infrastructure:

```
                                  +-----------------------+
                                  |   Ansible Control     |
                                  |        Node           |
                                  +-----------+-----------+
                                              |
      +------------------------+--------------+--------------+------------------------+
      |                        |                             |                        |
+-----v--------------+  +------v-------------+     +---------v----------+   +---------v----------+
|  Web & LB Tier     |  |   Database Tier    |     | Security & Vault   |   | Monitoring & Infra |
|  - HAProxy / Nginx |  |  - MySQL           |     | - System Hardening |   | - Async Tasks      |
|  - Apache / PHP    |  |  - PostgreSQL      |     | - AES256 Vault     |   | - Fact Caching     |
+--------------------+  +--------------------+     +--------------------+   +--------------------+
```

### Core Architecture Highlights:
* **Modular Role Design (`roles/`):** Clean separation of tasks, handlers, variables, defaults, templates, and metadata across all services.
* **Declarative Fault Tolerance:** Multi-tiered error recovery using `block`, `rescue`, `always`, and retry loops.
* **Zero-Downtime Multi-Tier Orchestration:** Sequential deployment via master `site.yml` playbooks with automated rollback safety hooks.
* **Zero-Trust Security:** AES256 encrypted variables using `ansible-vault` for passwords, private keys, and environment tokens.
* **High-Performance Execution:** Asynchronous job processing, pipeline optimization, parallel host strategy (`strategy: free`), and smart fact caching (`jsonfile`).

---

## 📚 Comprehensive Lab Index (Labs 01 - 20)

| Lab # | Module & Title | Key Concepts & Technologies |
| :--- | :--- | :--- |
| **Lab 01** | [Intro to Ansible & Control Node Setup](./lab-01-introduction-to-ansible/) | Ansible Engine installation, `/etc/ansible/hosts`, `ansible local -m ping`, local connection plugins. |
| **Lab 02** | [Inventory Management & Host Grouping](./lab-02-inventory-management/) | Static INI/YAML inventories, host/group variables, connection parameters (`ansible_user`, SSH keys). |
| **Lab 03** | [Ad-Hoc Commands & System Administration](./lab-03-adhoc-commands/) | One-liner command execution via `command`, `shell`, `copy`, `user`, and `service` ad-hoc modules. |
| **Lab 04** | [Playbook Fundamentals & Task Writing](./lab-04-playbooks-fundamentals/) | Playbook structure, tasks, modules syntax, idempotent state management, `ansible-playbook` execution. |
| **Lab 05** | [Variables, Facts & Custom Fact Gathering](./lab-05-variables-and-facts/) | `ansible_facts`, setup module, user-defined variables, `group_vars/`, `host_vars/`, custom `/etc/ansible/facts.d/`. |
| **Lab 06** | [Conditionals, Loops & Handlers](./lab-06-conditionals-loops-handlers/) | `when` statements, `loop`/`with_items`, event-driven `notify` handlers, changed-state triggers. |
| **Lab 07** | [Templates & Jinja2 Configuration](./lab-07-templates-and-jinja2/) | Dynamic config generation via `.j2` templates, filters, Jinja2 control structures (`for`, `if`), backup creation. |
| **Lab 08** | [File Management & Storage Operations](./lab-08-file-management/) | `file`, `copy`, `fetch`, `lineinfile`, `blockinfile`, `stat`, file permissions, ownership management. |
| **Lab 09** | [User Management, Security & SSH Keys](./lab-09-user-management/) | User account lifecycle, group creation, sudoers file management (`/etc/sudoers.d/`), SSH public key deployment. |
| **Lab 10** | [Package Management & System Updating](./lab-10-package-management/) | Package management across yum, dnf, and apt, repository updates, multi-package list installations. |
| **Lab 11** | [Service Management & Process Monitoring](./lab-11-service-management/) | Systemd service management (`started`, `restarted`, `enabled`), process monitoring, unit file configuration. |
| **Lab 12** | [Network & Firewall Automation](./lab-12-network-and-firewall/) | Firewall service management (`firewalld`, `ufw`), port opening (HTTP/HTTPS/SSH), network interface binding. |
| **Lab 13** | [Storage, Disk Partitioning & LVM](./lab-13-storage-and-lvm/) | Partition creation (`parted`), Logical Volume Management (`parted`, `pv`, `vg`, `lv`), filesystem formatting & mounting. |
| **Lab 14** | [System Hardening & Security Compliance](./lab-14-system-hardening/) | Kernel parameter tuning (`sysctl`), SSH daemon hardening (`sshd_config`), PAM policy alignment, audit compliance. |
| **Lab 15** | [Ansible Roles & Modular Architecture](./lab-15-ansible-roles/) | Enterprise role directory structure, role dependencies (`meta/main.yml`), role reusability, tag usage. |
| **Lab 16** | [Database Configuration & Management](./lab-16-database-management/) | Automated MySQL/MariaDB & PostgreSQL deployment, user privileges, Jinja2 configs, cron backups. |
| **Lab 17** | [Multi-Tier Application Stack Orchestration](./lab-17-multitier-stack-orchestration/) | End-to-end multi-tier stack (DB $\rightarrow$ Web $\rightarrow$ HAProxy), dynamic fact sharing (`hostvars`), automated rollback pipelines. |
| **Lab 18** | [Ansible Vault & Secret Security](./lab-18-ansible-vault-security/) | AES256 encryption (`ansible-vault`), `!vault` inline variables, multi-environment secrets (`group_vars/production`). |
| **Lab 19** | [Error Handling, Debugging & Check-Mode](./lab-19-error-handling-and-debugging/) | `debug` module, `--check` & `--diff` dry-runs, `ansible_check_mode`, `ignore_errors`, `block/rescue/always`. |
| **Lab 20** | [Optimizing Performance & Async Operations](./lab-20-optimizing-playbooks-and-performance/) | Role refactoring, background tasks (`async`/`poll`), delegation (`delegate_to`), `strategy: free`, benchmarking tools. |

---

## 📂 Repository Directory Structure

```text
ansible-automation-labs/
├── README.md
├── lab-01-introduction-to-ansible/
│   ├── inventory
│   └── verify-lab-completion.yml
├── lab-02-inventory-management/
├── lab-03-adhoc-commands/
├── lab-04-playbooks-fundamentals/
├── lab-05-variables-and-facts/
├── lab-06-conditionals-loops-handlers/
├── lab-07-templates-and-jinja2/
├── lab-08-file-management/
├── lab-09-user-management/
├── lab-10-package-management/
├── lab-11-service-management/
├── lab-12-network-and-firewall/
├── lab-13-storage-and-lvm/
├── lab-14-system-hardening/
├── lab-15-ansible-roles/
├── lab-16-database-management/
│   ├── site.yml
│   ├── inventory
│   └── roles/
│       ├── mysql_server/
│       └── postgresql_server/
├── lab-17-multitier-stack-orchestration/
│   ├── site.yml
│   ├── rollback.yml
│   ├── inventory
│   └── roles/
├── lab-18-ansible-vault-security/
│   ├── vault-secrets.yml
│   ├── manage_vault.sh
│   └── group_vars/
├── lab-19-error-handling-and-debugging/
│   ├── advanced-error-handling.yml
│   └── error-handling-template.yml
└── lab-20-optimizing-playbooks-and-performance/
    ├── optimized-playbook.yml
    ├── benchmark-playbooks.sh
    └── roles/
```

---

## ⚡ Prerequisites & Environment Setup

### Minimum Control Node Requirements:
* **OS:** RHEL 8/9, CentOS Stream, Ubuntu 20.04/22.04 LTS, or Debian 11/12
* **Python:** Python 3.8+
* **Ansible:** `ansible-core` 2.14+ or Ansible Community Package

### Fast Installation Commands:

```bash
# Ubuntu / Debian Control Node Setup
sudo apt update && sudo apt install -y ansible python3-pip git tree

# RHEL / CentOS Stream Control Node Setup
sudo dnf install -y epel-release
sudo dnf install -y ansible python3-pip git tree
```

---

## 🚀 How to Run & Verify Labs

Navigate to any target lab directory to run its playbooks and verification scripts:

### 1. Basic Playbook Execution
```bash
cd lab-16-database-management
ansible-playbook -i inventory site.yml
```

### 2. Dry-Run & Diff Mode (`--check --diff`)
Validate playbook execution logic without applying changes to target systems:
```bash
cd lab-19-error-handling-and-debugging
ansible-playbook -i inventory system-changes.yml --check --diff
```

### 3. Executing Encrypted Vault Playbooks
Pass password flags or automated password files:
```bash
cd lab-18-ansible-vault-security
# Interactive prompt
ansible-playbook -i inventory deploy-app-with-vault.yml --ask-vault-pass

# Non-interactive via Vault Password File
ansible-playbook -i inventory deploy-app-with-vault.yml --vault-password-file .vault_pass
```

### 4. Running Performance Benchmarks
Execute automated benchmarking scripts to measure timing across execution strategies:
```bash
cd lab-20-optimizing-playbooks-and-performance
./benchmark-playbooks.sh
```

### 5. Executing Verification Suites
Every lab includes an automated verification test suite:
```bash
ansible-playbook -i inventory verify-lab-completion.yml
```

---

## 🛡 Key Enterprise Features

### 1. Declarative Fault Recovery (`block/rescue/always`)
`Lab 19` demonstrates enterprise error handling where primary provisioning failures trigger alternative service setups, log post-mortems, and perform resource cleanups:

```yaml
tasks:
  - name: Resilient Web Provisioning
    block:
      - name: Attempt Primary Apache Installation
        package:
          name: httpd
          state: present
    rescue:
      - name: Fallback to Nginx Configuration
        package:
          name: nginx
          state: present
    always:
      - name: Record Audit Log Entry
        lineinfile:
          path: /var/log/ansible-deployment.log
          line: "Deployment attempt completed at {{ ansible_date_time.iso8601 }}"
```

### 2. Zero-Trust AES256 Vault Encryption
`Lab 18` enforces secrets security using inline and file-level Vault encryption, preventing sensitive credentials from leaking into plain text version control:

```yaml
# Encrypted Variable Definition
db_root_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          36626639613137613737613861343831343734323933393963383038316130313132333765366432
          3936306538353335343461623838383837333533373461310a303831313361363630323333333334
```

---

## 📄 License & Verification

All playbooks, roles, and scripts in this repository are released under the [MIT License](LICENSE). 

* **Maintainer:** DevOps & Automation Engineering Team
* **Curriculum Standard:** Red Hat Enterprise Linux (RHEL) Automation with Ansible
* **Portfolio Status:** Verified & Synchronized
