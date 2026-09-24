# Lab 19: Error Handling and Debugging in Ansible

## Overview
This directory contains production-grade Ansible playbooks demonstrating advanced debugging strategies, dry-run validations via `--check` mode, granular error suppression, and resilient fault-tolerant workflows using `block/rescue/always` paradigms.

## Key Features & Implementations
- **Variable Inspection & Debugging:** Detailed usage of `debug` module for lists, facts, conditions, and verbosity control (`-v`).
- **Check-Mode Safety (`ansible_check_mode`):** Implementation of dry-run aware logic preventing execution side-effects during audits (`--check --diff`).
- **Fault-Tolerant Block Structures:** Multi-tier fallback mechanisms (`block`, `rescue`, `always`) to recover from primary package/service failures.
- **Audit & Log Generation:** Automated post-mortem error logging and timestamped execution tracking.
- **Verification Suite:** Automated validation tests ensuring playbook resilience and structural integrity.

## Directory Structure
- `inventory` - Managed node inventory file.
- `debug-variables.yml` - Basic variable inspection playbook.
- `advanced-debug.yml` - Advanced filters, verbosity levels, and system facts debugging.
- `system-changes.yml` - System provisioning playbook designed for dry-run validation.
- `check-mode-aware.yml` - Playbook using `ansible_check_mode` conditional execution.
- `basic-error-handling.yml` - Demonstration of `ignore_errors` and error registration.
- `advanced-error-handling.yml` - Comprehensive `block/rescue/always` recovery pipeline.
- `error-handling-template.yml` - Reusable deployment and post-mortem logging template.
- `verify-lab-completion.yml` - Verification test suite for lab completion.
