# Introduction to Ansible

## Overview
This directory contains the initial environment setup and foundational ad-hoc connectivity tests for Ansible automation on a Linux control node using local connection plugins.

## Key Features & Implementations
- **Control Node Engine:** Installation and configuration of `ansible` engine via APT package manager.
- **Inventory Manifest (`inventory` & `/etc/ansible/hosts`):** Configuration of local target groups using `ansible_connection=local`.
- **Ad-hoc Execution:** Connectivity verification via `ansible local -m ping` ad-hoc module execution.
- **Verification Suite (`verify-lab-completion.yml`):** Automated test playbook verifying system facts and ping response.

## Directory Structure
- `inventory` - Project-level Ansible inventory manifest.
- `verify-lab-completion.yml` - Automated verification test suite.
