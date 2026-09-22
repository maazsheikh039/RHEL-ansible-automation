# Ansible Static & Dynamic Inventory Management

## Objectives
- Create and manage static Ansible inventories in INI and YAML formats.
- Implement host grouping, child-parent hierarchy, and variable mapping (host & group vars).
- Develop custom Python-based dynamic inventory scripts to query cloud provider infrastructures.
- Validate, inspect, and troubleshoot inventory configurations using Ansible CLI tools (`ansible-inventory`, `ansible-playbook`).

## Tools Used
- **Automation Framework:** Ansible CLI, Ansible-Inventory
- **Scripting & Logic:** Python 3 (JSON parsing, Environment variables manipulation)
- **Data Serialization Formats:** INI, YAML, JSON
- **Text Editors & Shell:** Bash CLI, Linux Utilities

## Key Skills Demonstrated
- Enterprise Ansible Inventory Architecture (Hierarchical Groups, Group Variables)
- Dynamic Infrastructure Discovery via Custom Python Scripts
- Variable Precedence and Dynamic Host Attribute Binding
- Dry-run validation and syntax troubleshooting for infrastructure-as-code

## Troubleshooting Log
1. **Dynamic Inventory List Slicing Bug Fix:**
   - *Issue:* In `cloud-inventory.py`, using static key slicing `list(self.inventory.keys())[1:-1]` included system keys like `all` in child group definitions, causing recursive parsing errors in Ansible.
   - *Fix:* Replaced static slicing with dynamic list comprehension filtering: `[g for g in self.inventory.keys() if g not in ['all', '_meta']]`.
2. **Offline Host Testing Support:**
   - *Issue:* Live SSH pings fail when managed node IP addresses are dummy lab values.
   - *Fix:* Integrated `--connection=local` and `gather_facts: no` flags in test playbooks to isolate inventory parsing logic from network dependencies.
