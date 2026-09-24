# Lab 18: Ansible Vault for Sensitive Data

## Overview
This directory contains production-ready Ansible Vault implementations for securing sensitive infrastructure secrets (database credentials, API tokens, SSL private keys) using AES256 encryption within Infrastructure-as-Code pipelines.

## Key Features & Implementations
- **File-Level Encryption (`vars/`):** Full AES256 file encryption for database, user, and API credential files.
- **Inline Variable Encryption (`vars/mixed_secrets.yml`):** Granular `!vault` string encryption embedded inside plain YAML structures.
- **Multi-Environment Isolation (`group_vars/`):** Environment-aware encrypted secrets separating `development` and `production` tiers.
- **Vault Password Management (`.vault_password`):** Non-interactive automated playbook execution via password file integration.
- **Management Utility Script (`manage_vault.sh`):** CLI wrapper for inspecting, editing, encrypting, and auditing project vault states.

## Directory Structure
- `inventory/hosts` - Inventory manifest with connection parameters.
- `vars/` - Encrypted variable files (`database_secrets.yml`, `user_secrets.yml`, `api_secrets.yml`, `mixed_secrets.yml`).
- `group_vars/` - Environment-specific variable overrides and encrypted vault files.
- `playbooks/secure_deployment.yml` - Secret-consuming deployment playbook.
- `playbooks/environment_deployment.yml` - Multi-environment deployment playbook.
- `templates/` - Dynamic configuration templates rendering secrets securely.
- `manage_vault.sh` - Vault status audit and management script.

