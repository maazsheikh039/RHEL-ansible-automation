#!/usr/bin/env python3
"""Advanced Dynamic Inventory Script - Cloud Simulator"""
import json
import sys
import os
from datetime import datetime

class CloudInventory:
    def __init__(self):
        self.inventory = {}
        self.read_environment()
        
    def read_environment(self):
        self.cloud_provider = os.environ.get('CLOUD_PROVIDER', 'aws')
        self.region = os.environ.get('CLOUD_REGION', 'us-east-1')
        self.environment = os.environ.get('ENVIRONMENT', 'production')
        
    def discover_instances(self):
        return [
            {'name': 'web1', 'ip': '192.168.1.10', 'type': 't2.micro', 'tags': {'Role': 'webserver', 'Environment': 'production'}},
            {'name': 'web2', 'ip': '192.168.1.11', 'type': 't2.micro', 'tags': {'Role': 'webserver', 'Environment': 'production'}},
            {'name': 'db1', 'ip': '192.168.1.20', 'type': 't2.small', 'tags': {'Role': 'database', 'Environment': 'production'}}
        ]
        
    def build_inventory(self):
        instances = self.discover_instances()
        self.inventory = {
            'all': {'vars': {'cloud_provider': self.cloud_provider, 'region': self.region, 'discovered_at': datetime.now().isoformat()}},
            '_meta': {'hostvars': {}}
        }
        
        for instance in instances:
            role = instance['tags'].get('Role', 'ungrouped')
            group_name = f"{role}s" if not role.endswith('s') else role
            
            if group_name not in self.inventory:
                self.inventory[group_name] = {'hosts': [], 'vars': {}}
            
            self.inventory[group_name]['hosts'].append(instance['name'])
            
            self.inventory['_meta']['hostvars'][instance['name']] = {
                'ansible_host': instance['ip'],
                'ansible_user': 'student',
                'instance_type': instance['type'],
                'cloud_provider': self.cloud_provider,
                'region': self.region
            }
            
            for tag_key, tag_value in instance['tags'].items():
                self.inventory['_meta']['hostvars'][instance['name']][f"tag_{tag_key.lower()}"] = tag_value
        
        env_group = f"{self.environment}_servers"
        # ⚠️ BUG FIXED: Exclude 'all' and '_meta' safely to prevent recursive inventory parsing errors
        self.inventory[env_group] = {
            'children': [g for g in self.inventory.keys() if g not in ['all', '_meta']]
        }
        return self.inventory
    
    def get_inventory(self):
        return self.build_inventory()
    
    def get_host_vars(self, hostname):
        inventory = self.get_inventory()
        return inventory.get('_meta', {}).get('hostvars', {}).get(hostname, {})

def main():
    cloud_inv = CloudInventory()
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        print(json.dumps(cloud_inv.get_inventory(), indent=2))
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        print(json.dumps(cloud_inv.get_host_vars(sys.argv[2]), indent=2))
    else:
        print("Usage: {} --list or {} --host <hostname>".format(sys.argv[0], sys.argv[0]))
        sys.exit(1)

if __name__ == '__main__':
    main()
