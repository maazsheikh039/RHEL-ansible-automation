# Lab 10: Managing Files with Ansible

## Overview
This lab demonstrates the configuration and deployment of static assets (`copy` module) and dynamic Jinja2 templated files (`template` module). It highlights variable inheritance across `group_vars` and `host_vars`, conditional Jinja2 processing, file permission enforcement, and automated verification playbooks.

## Key Files & Artifacts
- `static-files/` - Static configuration templates and binary assets
- `templates/` - Dynamic Jinja2 template files (`vhost.conf.j2`, `system-info.conf.j2`, `index.html.j2`)
- `group_vars/webservers.yml` & `host_vars/` - Variable definitions across host scopes
- `copy-static-files.yml` - Static file transfer playbook
- `deploy-templates.yml` - Jinja2 template deployment engine
- `advanced-file-management.yml` - Comprehensive multi-module file orchestrator
- `test-file-management.yml` - Verification testing suite
