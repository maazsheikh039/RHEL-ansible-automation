# Lab 15: Configuring Web Servers with Ansible

## Overview
This directory contains production-ready Ansible playbooks for automated Apache HTTP server provisioning, dynamic web page rendering using Jinja2 templates, static asset deployment, firewalld integration, and post-deployment validation.

## Key Features & Implementations
- **Declarative Web Server Provisioning:** Automated installation and lifecycle management of `httpd` across RHEL/CentOS enterprise nodes.
- **Dynamic Jinja2 Templating:** Rendered server-specific properties (`hostname`, `IP address`, `distribution`, `timestamp`) into web templates (`templates/index.html.j2` & `templates/httpd.conf.j2`).
- **Handler-driven Workflows:** Triggered zero-downtime service reloads (`reload apache`) and full service restarts (`restart apache`) upon configuration drifts.
- **Firewall Integration:** Managed HTTP service availability dynamically via `ansible.posix.firewalld`.
- **Validation Pipeline:** Automated verification testing using `uri` probes, TCP port wait checks, and HTTP header auditing.

## Directory Structure
- `inventory/hosts.ini` - Inventory manifest with connection variables.
- `playbooks/install-apache.yml` - Package installation and base Apache configuration.
- `playbooks/deploy-website.yml` - Web asset, Jinja2 template, and HTML deployment.
- `playbooks/complete-webserver-setup.yml` - Master orchestration playbook with task includes.
- `playbooks/deploy-content.yml` - Task module for web content rendering.
- `playbooks/verify-deployment.yml` - Post-deployment validation test suite.
- `templates/` - Jinja2 configuration templates (`httpd.conf.j2`, `index.html.j2`).
- `files/` - Static site assets (`style.css`).
