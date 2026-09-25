# Enterprise Ansible Infrastructure-as-Code (IaC) & Automation Platform

[![Ansible Core](https://img.shields.io/badge/Ansible-2.14+-EE0000?style=for-the-badge&logo=ansible&logoColor=white)](https://www.ansible.com/)
[![IaC Status](https://img.shields.io/badge/IaC-Production--Ready-success?style=for-the-badge&logo=terraform&logoColor=white)](https://github.com/)
[![Security](https://img.shields.io/badge/Security-AES256%20Vault-red?style=for-the-badge&logo=1password&logoColor=white)](https://docs.ansible.com/ansible/latest/vault_guide/index.html)

Welcome to the **Enterprise Ansible Infrastructure as Code (IaC) & Automation Platform** master repository. This repository contains an end-to-end, enterprise-grade automation engine built with Ansible. Designed for high availability, security hardening, and scalable multi-tier environment provisioning, this project demonstrates operational excellence in infrastructure management, configuration management, and DevOps workflow orchestration.

Designed according to Red Hat Enterprise Linux (RHEL) Automation standards and Red Hat Ansible Automation Platform (AAP) best practices, this repository serves as a production-grade reference architecture for DevOps and Automation Engineers.

---

## 📋 Table of Contents

- [Architectural Overview & Core Capabilities](#-architectural-overview--core-capabilities)
- [Architectural Highlights](#-architectural-highlights)
- [Repository Directory Structure](#-repository-directory-structure)
- [Prerequisites & Environment Setup](#-prerequisites--environment-setup)
- [How to Run & Verify Playbooks](#-how-to-run--verify-playbooks)
- [Key Enterprise Features](#-key-enterprise-features)
- [License & Legal Terms](#-license--legal-terms)

---

## 🏗 Architectural Overview & Core Capabilities

This repository demonstrates end-to-end automation capability across enterprise IT infrastructure:

```text
                                  +-----------------------+
                                  |   Ansible Control     |
                                  |        Node           |
                                  +-----------+-----------+
                                              |
      +------------------------+--------------+--------------+------------------------+
      |                        |                             |                        |
+-----v--------------+  +------v-------------+     +---------v----------+   +---------v----------+
|  Web & LB Tier     |  |    Database Tier   |     | Security & Vault   |   | Monitoring & Infra |
|  - HAProxy / Nginx |  |  - MySQL           |     | - System Hardening |   | - Async Tasks      |
|  - Apache / PHP    |  |  - PostgreSQL      |     | - AES256 Vault     |   | - Fact Caching     |
+--------------------+  +--------------------+     +--------------------+   +--------------------+


💡 Architectural Highlights
1. Multi-Tier Infrastructure Orchestration
Declarative Web & Application Stack: Automated deployment of high-performance web tiers, reverse proxies, load balancers, and database clusters.

Inter-Host Context Passing: Dynamic variable registration (set_fact and hostvars) enabling inter-system communication across multi-tier node clusters.

High Availability & Traffic Routing: Automated configuration of HAProxy load balancers and web backend pool synchronization.

Automated Rollback Engine: Resilient deployment pipelines equipped with failure handling, resource cleanup, and immediate environment restoration mechanisms.

2. Database Provisioning & Management
Multi-Engine Support: Declarative installation, initialization, and configuration of relational database servers (MySQL and PostgreSQL).

Least-Privilege Security Scoping: Fine-grained user access controls, host-based binding, and custom privilege assignment.

Database Backup & Lifecycle Automation: Automated backup generation scripts, data retention scheduling, and cron job management.

3. Enterprise Security & Secret Hardening
AES-256 Vault Encryption: Strict isolation of sensitive credentials, API keys, certificates, and database access tokens using Ansible Vault.

Granular Secret Architecture: Multi-environment secret separation (development vs production) supporting inline and file-level encryption.

Host Hardening & Network Security: Dynamic firewall policy management (firewalld, ufw), service port restrictions, and security baseline controls.

4. Performance Optimization & Scalability
Modular Role Design: High-level playbook decomposition into reusable, modular Ansible roles.

Asynchronous Processing: Non-blocking task execution (async / poll) for long-running system updates and service initializations.

Parallel Strategy Tuning: Optimized execution forks, control node task delegation (delegate_to), and SSH connection pipelining.

Fact Caching & Performance Auditing: Smart JSON fact caching and automated benchmarking suites for measuring execution latency.

5. Resilient Error Handling & Quality Assurance
Dry-Run Validation: Non-intrusive syntax checks, dry-runs (--check), and execution diffing (--diff).

Declarative Fault Recovery: block / rescue / always exception handling patterns for automated issue mitigation and post-mortem logging.

Automated Verification Pipelines: Post-deployment status reporting, network socket probing, and active service health monitoring.

📂 Repository Directory Structure
.
├── group_vars/             # Global & environment-specific variable declarations
├── host_vars/              # Target-specific node configurations
├── inventory/              # Infrastructure manifests (static & dynamic)
├── playbooks/              # Orchestration entrypoints, testing & rollback workflows
├── roles/                  # Modular Ansible roles (Web, DB, Security, App)
├── templates/              # Dynamic Jinja2 configuration templates
├── manage_vault.sh         # Custom security vault audit and utility tool
├── benchmark-playbooks.sh  # Execution performance measurement suite
├── ansible.cfg             # Optimized Ansible engine configuration
└── LICENSE                 # Custom View-Only License terms

# Ubuntu / Debian Control Node Setup
sudo apt update && sudo apt install -y ansible python3-pip git tree

# RHEL / CentOS Stream Control Node Setup
sudo dnf install -y epel-release
sudo dnf install -y ansible python3-pip git tree

🚀 How to Run & Verify Playbooks
1. Basic Playbook Execution
Bash
ansible-playbook -i inventory/hosts playbooks/site.yml
2. Dry-Run & Diff Mode (--check --diff)
Validate playbook execution logic without applying changes to target systems:

Bash
ansible-playbook -i inventory/hosts playbooks/site.yml --check --diff
3. Executing Encrypted Vault Playbooks
Pass password flags or automated password files:

Bash
# Interactive prompt
ansible-playbook -i inventory/hosts playbooks/site.yml --ask-vault-pass

# Non-interactive via Vault Password File
ansible-playbook -i inventory/hosts playbooks/site.yml --vault-password-file .vault_password
4. Running Performance Benchmarks
Execute automated benchmarking scripts to measure timing across execution strategies:

Bash
./benchmark-playbooks.sh
5. Executing Verification Suites
Execute automated verification pipelines across deployed environments:

Bash
ansible-playbook -i inventory/hosts playbooks/verify-deployment.yml
🛡 Key Enterprise Features
1. Declarative Fault Recovery (block/rescue/always)
Demonstrates enterprise error handling where primary provisioning failures trigger alternative service setups, log post-mortems, and perform resource cleanups:

YAML
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
2. Zero-Trust AES256 Vault Encryption
Enforces secrets security using inline and file-level Vault encryption, preventing sensitive credentials from leaking into plain text version control:

YAML
# Encrypted Variable Definition
db_root_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          36626639613137613737613861343831343734323933393963383038316130313132333765366432
          3936306538353335343461623838383837333533373461310a303831313361363630323333333334


⚖️ License & Legal Terms
Copyright (c) 2026 Maaz Ghufran. All Rights Reserved.

This repository and all associated files are the exclusive property of Maaz Ghufran.

Permitted Use: Viewing and reading the content solely for educational, assessment, or portfolio/hiring evaluation purposes.

Restrictions: Copying, reproducing, modifying, altering, distributing, sublicensing, or deploying any portion of this codebase without explicit written permission is strictly prohibited.

For complete legal terms, please refer to the LICENSE file.




