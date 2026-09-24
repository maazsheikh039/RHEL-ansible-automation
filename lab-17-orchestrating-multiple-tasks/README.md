# Lab 17: Orchestrating Multiple Tasks with Ansible

## Overview
This repository contains production-grade Ansible playbooks for orchestrating a multi-tier enterprise web application architecture (MariaDB Database, Apache/PHP Web Tier, and HAProxy Load Balancer) with strict inter-system dependency enforcement and automated rollback strategies.

## Highlights & Architecture
- **Master Entrypoint (`site.yml`):** Orchestrates multi-phase playbooks (`database.yml`, `webservers.yml`, `loadbalancer.yml`, `monitoring.yml`).
- **Inter-Host Fact Sharing (`hostvars`):** Dynamically passes database IP and hostname context to application and load balancer nodes.
- **Dependency Validation (`dependency_check.yml`):** Verifies disk space, network latency, and open socket availability before provisioning.
- **HAProxy Load Balancing (`haproxy.cfg.j2`):** Dynamically loops through active web tier inventory to register round-robin backends.
- **Automated Rollback Engine (`rollback.yml`):** Cleans up app files, terminates system services, and retracts firewall rules during failures.

## Directory Structure
- `inventory/hosts` - Inventory manifest with connection parameters.
- `group_vars/all.yml` - Global variables and deployment settings.
- `playbooks/site.yml` - Master orchestration playbook.
- `playbooks/dependency_check.yml` - System prerequisite verification playbook.
- `playbooks/database.yml` - MariaDB deployment playbook.
- `playbooks/webservers.yml` - Apache/PHP web tier deployment playbook.
- `playbooks/loadbalancer.yml` - HAProxy load balancer setup playbook.
- `playbooks/monitoring.yml` - Monitoring script setup and stack validation playbook.
- `playbooks/rollback.yml` - System state restoration and cleanup playbook.
- `templates/` - Dynamic Jinja2 configuration templates (`app_config.php.j2`, `webapp.conf.j2`, `haproxy.cfg.j2`).
