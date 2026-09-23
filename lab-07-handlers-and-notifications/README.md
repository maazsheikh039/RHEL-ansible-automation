# Lab 07: Handlers and Notifications in Ansible

## Overview
This lab covers the design, implementation, and optimization of Ansible handlers and `notify` directives. It demonstrates asynchronous task notifications, idempotency protection, handler chaining, immediate execution using `meta: flush_handlers`, and production service reloads with pre-flight syntax validation.

## Files Included
- `basic-handler.yml` - Basic task notification and service restart workflow
- `multiple-handlers.yml` - Demonstrates handler chaining (validation, reload, and logging)
- `flush-handlers.yml` - Implements `meta: flush_handlers` for mid-play service verification
- `real-world-nginx-handlers.yml` - Production Nginx template deployment with syntax-checked reloads
- `templates/nginx.conf.j2` - Dynamic Jinja2 configuration template for Nginx
- `verify-lab.yml` - Automated verification playbook to audit system state
