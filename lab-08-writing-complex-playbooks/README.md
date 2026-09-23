# Lab 08: Writing Complex Playbooks & Roles Architecture

## Overview
This lab demonstrates multi-play Ansible architecture, role-based infrastructure orchestration (`mysql`, `apache`, `webapp`), centralized `group_vars` variable management, Jinja2 template rendering, pre/post task validation, and automated environment auditing.

## Architecture & Structural Breakdown
- `site.yml` - Multi-play orchestration playbook
- `complete-deployment.yml` - Enterprise playbook featuring pre/post tasks, handlers, and dynamic reporting
- `group_vars/` - Environmental variable segregation (`all.yml`, `web_servers.yml`, `database_servers.yml`)
- `roles/mysql/` - MySQL database deployment role
- `roles/apache/` - Apache HTTP web server role
- `roles/webapp/` - Modular PHP application deployment role
- `test-deployment.yml` - Deployment audit and verification playbook
