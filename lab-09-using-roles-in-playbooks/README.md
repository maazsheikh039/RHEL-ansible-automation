# Lab 09: Using Roles in Playbooks

## Overview
This lab demonstrates the creation, structure, and execution of production-ready Ansible Roles (`apache-webserver` and `common`). It covers role directory hierarchies, J2 templating, handler notifications, variable precedence (`defaults/` vs `vars/`), multi-role orchestration in `site.yml`, and automated assertion testing.

## Key Files & Artifacts
- `roles/apache-webserver/` - Complete Apache Web Server installation and virtual host management role
- `roles/common/` - Base system setup role
- `deploy-webserver.yml` - Basic role deployment playbook
- `deploy-webserver-advanced.yml` - Advanced role deployment with custom overrides
- `site.yml` - Multi-role master playbook
- `validate-deployment.yml` - Automated deployment assertion and test suite
- `role-structure-guide.txt` - Architectural breakdown of Ansible role directories
