# Enterprise Ansible Playbook Automation & Dynamic Templating

## Objectives
- Implement modular Ansible Playbooks with declarative task states.
- Configure Jinja2 dynamic templating for web server configuration rendering.
- Implement robust error handling strategies using `ignore_errors` and `block/rescue/always` blocks.
- Manage targeted executions using Ansible Tags and external variable files (`vars_files`).

## Tools Used
- **Automation Engine:** Ansible Core
- **Templating Engine:** Jinja2
- **Operating System:** Red Hat Enterprise Linux / CentOS
- **Target Service:** Apache HTTP Server (`httpd`)

## Key Skills Demonstrated
- IaC (Infrastructure as Code) workflow development.
- Error-tolerant playbook architecture.
- Modular variable abstraction and state management.
- Dynamic web content provisioning based on system facts.

## Troubleshooting Log
1. **Unreachable SSH Node Fallback:** Updated hardcoded `192.168.1.x` inventory targets to local connection contexts (`ansible_connection=local`) to allow standalone terminal validation.
2. **Package Engine Modernization:** Replaced deprecated `yum` references with generic `package` modules.
3. **Fact Parsing Resilience:** Added Jinja2 default filters (`default('127.0.0.1')`) to handle missing or unassigned network interface facts seamlessly.
