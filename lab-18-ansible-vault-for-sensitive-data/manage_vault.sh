#!/bin/bash

VAULT_PASSWORD_FILE=".vault_password"

case "$1" in
    "encrypt")
        if [ -z "$2" ]; then
            echo "Usage: $0 encrypt <file>"
            exit 1
        fi
        ansible-vault encrypt "$2" --vault-password-file "$VAULT_PASSWORD_FILE"
        ;;
    "decrypt")
        if [ -z "$2" ]; then
            echo "Usage: $0 decrypt <file>"
            exit 1
        fi
        ansible-vault decrypt "$2" --vault-password-file "$VAULT_PASSWORD_FILE"
        ;;
    "view")
        if [ -z "$2" ]; then
            echo "Usage: $0 view <file>"
            exit 1
        fi
        ansible-vault view "$2" --vault-password-file "$VAULT_PASSWORD_FILE"
        ;;
    "edit")
        if [ -z "$2" ]; then
            echo "Usage: $0 edit <file>"
            exit 1
        fi
        ansible-vault edit "$2" --vault-password-file "$VAULT_PASSWORD_FILE"
        ;;
    "status")
        echo "=== Vault Files Encryption Audit ==="
        find . -name "*.yml" -type f | while read file; do
            if head -1 "$file" 2>/dev/null | grep -q "ANSIBLE_VAULT"; then
                echo "✓ $file (encrypted)"
            else
                echo "○ $file (plain text)"
            fi
        done
        ;;
    *)
        echo "Usage: $0 {encrypt|decrypt|view|edit|status} [file]"
        exit 1
        ;;
esac
