# Lab 12: Automated User and Group Management with Ansible

## Overview
This repository contains production-ready Ansible playbooks for automated identity management, Role-Based Access Control (RBAC), home directory migration, and compliance verification across Enterprise Linux environments.

## Architecture Highlights
- **Declarative RBAC:** Standardized GIDs and UIDs for developers, testers, managers, contractors, and sysadmins.
- **Dynamic Iteration:** Advanced variable mapping using `with_nested` for structure creation.
- **Security Hardening:** Shell restrictions (`/bin/sh`), account locking (`password_lock`), and password aging via `chage`.
- **Automated Audit Engine:** Declarative testing framework using `stat` and `getent` modules.

## File Structure
- `inventory.ini` - Local host connections inventory.
- `create-groups.yml` - Group infrastructure creation.
- `create-users.yml` - Initial user provisioning.
- `modify-shells.yml` - Shell modification and fallback handling.
- `modify-groups.yml` - Dynamic supplementary group membership updates.
- `modify-home-dirs.yml` - Custom home path migration and directory setup.
- `advanced-user-management.yml` - Complex user workflows and audit reporting.
- `verify-user-management.yml` - Automated compliance assertion test suite.
