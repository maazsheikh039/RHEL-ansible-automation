# Lab 16: Database Configuration with Ansible

## Overview
This directory contains production-ready Ansible playbooks and a unified, reusable role (`database-management`) for automated installation, configuration, user/database provisioning, security hardening, and scheduled backups for both MySQL and PostgreSQL database servers.

## Key Features & Implementations
- **MySQL Automation (`playbooks/mysql-setup.yml`):** Automated installation of MySQL Server, root password configuration, database/user creation, and remote access binding.
- **PostgreSQL Automation (`playbooks/postgresql-setup.yml`):** Provisioning of PostgreSQL Server, database creation, user role attributes, `pg_hba.conf` authentication, and privilege management.
- **Reusable Database Role (`roles/database-management/`):** Dynamic parameterized role supporting both MySQL and PostgreSQL via `database_type` variable.
- **Security Hardening (`security.yml`):** Integration with UFW firewall and fail2ban for port access controls.
- **Automated Backups (`backup.yml`):** Shell backup scripts (`mysql-backup.sh.j2`, `postgresql-backup.sh.j2`) and automated daily cron jobs.

## Directory Structure
- `inventory.ini` - Database servers inventory manifest.
- `playbooks/mysql-setup.yml` - Standalone MySQL setup playbook.
- `playbooks/postgresql-setup.yml` - Standalone PostgreSQL setup playbook.
- `playbooks/role-mysql.yml` - Role execution playbook for MySQL.
- `playbooks/role-postgresql.yml` - Role execution playbook for PostgreSQL.
- `roles/database-management/` - Parameterized database role (tasks, templates, defaults, handlers, meta).
