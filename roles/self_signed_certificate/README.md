<!-- BEGIN_ANSIBLE_DOCS -->

# Ansible Role: trippsc2.general.self_signed_certificate
Version: 2.6.2

This role generates a self-signed TLS certificate.

## Requirements

| Platform | Versions |
| -------- | -------- |
| Debian | <ul><li>bullseye</li><li>bookworm</li></ul> |
| EL | <ul><li>8</li><li>9</li></ul> |
| Ubuntu | <ul><li>focal</li><li>jammy</li><li>noble</li></ul> |
| Windows | <ul><li>2019</li><li>2022</li></ul> |

## Dependencies
| Role |
| ---- |
| trippsc2.general.generate_csr |

| Collection |
| ---------- |
| ansible.windows |
| community.crypto |

## Role Arguments
|Option|Description|Type|Required|Choices|Default|
|---|---|---|---|---|---|
| cert_certificate_owner | <p>The owner of the certificate on Linux systems.</p><p>On Windows systems, this is ignored.</p> | str | no |  | root |
| cert_certificate_group | <p>The group of the certificate on Linux systems.</p><p>On Windows systems, this is ignored.</p> | str | no |  | root |
| cert_certificate_mode | <p>The mode of the certificate on Linux systems.</p><p>On Windows systems, this is ignored.</p> | str | no |  | 0644 |


## License
MIT

## Author and Project Information
Jim Tarpley
<!-- END_ANSIBLE_DOCS -->
