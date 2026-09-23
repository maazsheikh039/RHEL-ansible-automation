# Lab 04: Introduction to Ansible Modules

## Overview
This lab covers working with core Ansible modules (`yum`, `apt`, `service`, `package`, `copy`, `debug`) for cross-platform Linux system administration, service orchestration, block structures, and error handling mechanisms.

## Files Included
- `package-management.yml` - YUM package management for Red Hat family
- `apt-management.yml` - APT package management for Debian family
- `universal-packages.yml` - Cross-platform package installation using OS facts
- `service-management.yml` - Web service setup and status registration
- `advanced-services.yml` - Structured blocks for SSH and firewall configuration
- `infrastructure-setup.yml` - Complete multi-tier infrastructure setup with handlers
- `error-handling.yml` - Resilience patterns (`ignore_errors`, `failed_when`, `until/retries`)
