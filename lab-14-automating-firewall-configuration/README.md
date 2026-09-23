# Lab 14: Automating Firewall Configuration with Ansible and Firewalld

## Overview
This directory contains production-ready Ansible playbooks for managing declarative host firewall policies, zone segmentation, custom XML service definitions, rich rules, and automated audit/compliance verification using `ansible.posix.firewalld`.

## Highlights & Features
- **Declarative Policy Engine:** Uses `ansible.posix.firewalld` with `permanent: yes` and `immediate: yes` for zero-downtime, reboot-persistent rule enforcement.
- **Multi-Tier Role Isolation:** Enforces Web Tier (`public` zone, HTTP/8080) and Database Tier (`internal` zone, IP-restricted MySQL/3306) security architectures.
- **Custom XML Application Services:** Deploys custom `/etc/firewalld/services/custom-app.xml` templates for non-standard enterprise applications.
- **Granular Rich Rules:** Implements CIDR-based access controls, SSH rate-limiting (`limit value="3/m"`), and audit logging (`drop log prefix`).
- **Automated Verification Pipeline:** Probes port states (`wait_for`), checks policy compliance, and backs up active configurations.

## File Structure
- `inventory` - Environment connection manifest.
- `basic-firewall.yml` - Systemd firewalld state management and default service enablement (`ssh`, `http`, `https`).
- `advanced-firewall.yml` - Port binding, dynamic ranges (`60000-61000/tcp`), and explicit service blocking.
- `rich-rules.yml` - CIDR restriction, rate limiting, and drop packet logging rules.
- `zones-management.yml` - DMZ custom zone creation, interface mapping, and source binding.
- `services-management.yml` - Custom XML service deployment (`custom-app.xml`) and legacy service teardown.
- `security-policy.yml` - End-to-end multi-tier role-based firewall security policy execution.
- `firewall-testing.yml` - Automated socket probing and remote configuration audit fetcher.
- `troubleshoot-firewalld.yml` - Diagnostic playbook for firewalld service recovery and iptables conflict remediation.
- `backups/` - Locally retrieved active firewall state backups per target node.
