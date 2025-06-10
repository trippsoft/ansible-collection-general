<!-- BEGIN_ANSIBLE_DOCS -->

# Ansible Role: trippsc2.general.self_signed_certificate
Version: 2.10.1

This role generates a self-signed TLS certificate.

The role depends on the `trippsc2.general.generate_csr` role to generate a private key and CSR.

The role does the following:
  - Runs the `trippsc2.general.generate_csr` role to generate a private key and CSR, if needed.
  - If the private key and CSR are generated, the role generates a self-signed certificate and stores it in the `cert_certificate_content` variable.
  - Optionally, the role will save the certificate to a file.


## Requirements

| Platform | Versions |
| -------- | -------- |
| Debian | <ul><li>bookworm</li></ul> |
| EL | <ul><li>9</li><li>8</li></ul> |
| Fedora | <ul><li>all</li></ul> |
| Ubuntu | <ul><li>noble</li><li>jammy</li><li>focal</li></ul> |
| Windows | <ul><li>all</li></ul> |

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
| cert_certificate_to_file | <p>Whether to generate the certificate to a file.</p><p>If set to `true`, the certificate will be stored in the `cert_certificate_content` variable.</p> | bool | no |  | True |
| cert_certificate_path | <p>The path to the certificate file to generate.</p><p>If *cert_certificate_to_file* is `true`, this is required.</p> | path | no |  |  |
| cert_certificate_owner | <p>The owner of the certificate on Linux systems.</p><p>On Windows systems, this is ignored.</p> | str | no |  | root |
| cert_certificate_group | <p>The group of the certificate on Linux systems.</p><p>On Windows systems, this is ignored.</p> | str | no |  | root |
| cert_certificate_mode | <p>The mode of the certificate on Linux systems.</p><p>On Windows systems, this is ignored.</p> | str | no |  | 0644 |
| cert_not_after | <p>The date and time when the certificate will expire.</p><p>Refer to the **community.crypto.x509_certificate** module for the format.</p><p>If not provided, the certificate will expire in 3650 days.</p> | str | no |  |  |


## License
MIT

## Author and Project Information
Jim Tarpley (@trippsc2)
<!-- END_ANSIBLE_DOCS -->
