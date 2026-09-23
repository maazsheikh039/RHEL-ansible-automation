# Lab 13: Network Automation with Ansible and NetworkManager

## Overview
This repository contains production-ready Ansible playbooks for declaratively automating NetworkManager interfaces, static IPv4 assignments, custom routing tables, Jinja2 templated DNS configurations, and validation testing.

## Architecture Highlights
- **Declarative NetworkManager (`nmcli`):** Programmatically provisions primary and secondary interfaces without manual XML/ifcfg editing.
- **Advanced Static Routing:** Applies static route blocks persistent across reboots via `/etc/sysconfig/network-scripts/route-*`.
- **Templated Resolver Configuration:** Jinja2 `resolv.conf.j2` dynamic rendering with search domains and failover DNS parameters.
- **Audit & Compliance Fetcher:** Automated validation suite gathering interface states and saving remote system reports locally.

## File Structure
- `inventory` - Ansible host connectivity configuration.
- `configure-static-ip.yml` - Static IP address provisioning playbook.
- `configure-secondary-interface.yml` - Secondary network interface setup playbook.
- `configure-routing.yml` - Custom static routing table configuration playbook.
- `configure-dns.yml` - DNS configuration and Jinja2 template deployment playbook.
- `templates/resolv.conf.j2` - Jinja2 template for `/etc/resolv.conf`.
- `master-network-config.yml` - Unified network provisioning and connectivity testing.
- `validate-network.yml` - Network state audit and report fetcher playbook.
- `reports/` - Collected network configuration audit reports per managed node.
