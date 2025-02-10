<!-- BEGIN_ANSIBLE_DOCS -->

# Ansible Role: trippsc2.general.rotate_linux_password
Version: 2.6.4

This role rotates a Linux user password.

## Requirements

| Platform | Versions |
| -------- | -------- |
| Debian | <ul><li>bullseye</li><li>bookworm</li></ul> |
| EL | <ul><li>8</li><li>9</li></ul> |
| Ubuntu | <ul><li>focal</li><li>jammy</li><li>noble</li></ul> |

## Dependencies

None.

## Role Arguments
|Option|Description|Type|Required|Choices|Default|
|---|---|---|---|---|---|
| vault_url | <p>The URL for accessing HashiCorp Vault.</p><p>Alternatively, this can be configured through ansible.cfg or environment variables.</p><p>If *rotate_use_vault* is `false`, this is ignored.</p> | str | no |  |  |
| vault_token | <p>The token for accessing HashiCorp Vault.</p><p>Alternatively, this (or any other authentication method) can be configured through ansible.cfg or environment variables.</p><p>If *rotate_use_vault* is `false`, this is ignored.</p> | str | no |  |  |
| rotate_use_vault | <p>Whether to use HashiCorp Vault to store the new password.</p> | bool | no |  | True |
| rotate_create_vault_mount_point | <p>Whether to create the HashiCorp Vault mount point, if needed.</p><p>If *rotate_use_vault* is `false`, this is ignored.</p> | bool | no |  | True |
| rotate_force_password_change | <p>Whether to change the password always without checking the age.</p><p>If set to `true`, this role is not idempotent.</p> | bool | no |  | False |
| rotate_vault_mount_point | <p>The mount point for the KV2 secrets engine in HashiCorp Vault.</p><p>If *rotate_use_vault* is `true`, this is required. Otherwise, it is ignored.</p> | str | no |  |  |
| rotate_vault_secret_path | <p>The path to the secret in HashiCorp Vault.</p><p>If *rotate_use_vault* is `true`, this is required. Otherwise, it is ignored.</p> | str | no |  |  |
| rotate_user | <p>The user whose password will be rotated.</p> | str | yes |  |  |
| rotate_new_password | <p>The new password for the user.</p><p>If *rotate_use_vault* is `false`, this is required. Otherwise, the new password will be stored in HashiCorp Vault when rotated.</p> | str | no |  |  |


## License
MIT

## Author and Project Information
Jim Tarpley
<!-- END_ANSIBLE_DOCS -->
