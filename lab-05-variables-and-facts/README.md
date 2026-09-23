# Lab 05: Variables and Facts

## Overview
This lab covers Ansible variable scopes (playbook, group_vars, host_vars), custom local fact deployment (`/etc/ansible/facts.d`), fact-driven OS/hardware task adaptation, dynamic variable assignment using `set_fact`, and automated testing using the `assert` module.

## Files Included
- `variables-demo.yml` - Demonstrates variable data types and dictionary references
- `external-vars-demo.yml` - Implements external variable loading from `group_vars/all.yml`
- `facts-exploration.yml` - Displays system, network, and disk facts
- `setup-custom-facts.yml` - Provisions JSON/INI custom facts on managed nodes
- `display-custom-facts.yml` - Retrieves custom facts from `ansible_local`
- `os-specific-tasks.yml` - Cross-distribution web server provisioning driven by OS family facts
- `version-specific-tasks.yml` - Package and service handling based on major OS release
- `hardware-based-tasks.yml` - Dynamically generates app configurations based on RAM and CPU core counts
- `variable-precedence.yml` - Illustrates precedence hierarchy across host_vars, set_fact, and registered vars
- `dynamic-variables.yml` - Generates calculated facts dynamically at runtime
- `lab5-verification.yml` - Assertion-driven verification playbook
