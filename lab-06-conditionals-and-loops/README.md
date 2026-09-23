# Lab 06: Conditionals and Loops in Ansible

## Overview
This lab demonstrates Ansible conditional execution using `when` statements, iterative processing using `loop` and `loop_control`, dynamic variable mapping with Jinja2 filters (`dict2items`), and multi-environment playbook orchestration with error handling mechanisms.

## Files Included
- `basic-conditionals.yml` - Demonstrates basic conditional execution based on variables and facts
- `advanced-conditionals.yml` - Implements memory checks, date evaluations, and package presence conditionals
- `basic-loops.yml` - Iterates over simple lists to manage packages, users, and directories
- `advanced-loops.yml` - Processes complex data structures and converts dictionaries via `dict2items`
- `loop-control.yml` - Configures custom loop variables, index tracking, and pause delays
- `combined-logic.yml` - Integrates conditionals and loops for role-based software deployment
- `error-handling.yml` - Validates service states and captures loop output using `register`
- `multi-environment-deploy.yml` - Orchestrates complete deployments across development, staging, and production
- `templates/app-config.j2` - Dynamic Jinja2 configuration template
- `verify-lab.yml` - Verification playbook for inspecting lab state
