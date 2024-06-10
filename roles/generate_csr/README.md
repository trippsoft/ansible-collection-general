<!-- BEGIN_ANSIBLE_DOCS -->

# Ansible Role: trippsc2.generate_csr
This role generates a Certificate Signing Request (CSR) for a Linux or Windows machine, if an existing certificate doesn't exist or needs renewal.

## Requirements

| Platform | Versions |
| -------- | -------- |
| EL | 8 |
| Windows | 2019, 2022 |

## Dependencies

| Collection |
| ---------- |
| ansible.windows |
| community.crypto |

## Role Arguments
|Option|Description|Type|Required|Choices|Default|
|---|---|---|---|---|---|
| cert_force_regenerate | Whether to force regeneration of the CSR, even if the certificate is not near expiration. If `true`, the role will not be idempotent. | bool | no |  | false |
| cert_certifcate_path | The path to the certificate file to generate. On Debian-based Linux, this defaults to `/etc/ssl/certs/cert.crt`. On Red Hat-based Linux, this defaults to `/etc/pki/tls/certs/cert.crt`. On Windows, this defaults to `C:\Windows\Temp\cert.crt`. | path | no |  | OS Specific |
| cert_regenerate_days | The number of days before the certificate expiration to regenerate the CSR. | int | no |  | 30 |
| cert_private_key_path | The path to the private key file to generate. On Debian-based Linux, this defaults to `/etc/ssl/private/cert.key`. On Red Hat-based Linux, this defaults to `/etc/pki/tls/private/cert.key`. On Windows, this defaults to `C:\Windows\Temp\cert.key`. | path | no |  | OS Specific |
| cert_private_key_owner | The owner of the private key on Linux systems. | str | no |  | root |
| cert_private_key_group | The group of the private key on Linux systems. | str | no |  | root |
| cert_private_key_mode | The mode of the private key on Linux systems. | str | no |  | 0600 |
| cert_private_key_type | The type of private key to generate. | str | no | <ul><li>DSA</li><li>ECC</li><li>Ed25519</li><li>Ed448</li><li>RSA</li><li>X25519</li><li>X448</li></ul> | RSA |
| cert_private_key_size | The size of the private key to generate. | int | no |  | 2048 |
| cert_backup_replaced_private_key | Whether to backup the replaced private key. | bool | no |  | true |
| cert_common_name | The Common Name (CN) of the certificate. | str | no |  | {{ inventory_hostname }} |
| cert_subject_alternative_names | The Subject Alternative Names (SANs) of the certificate. DNS names should be prefixed with `DNS:` and IP addresses should be prefixed with `IP:`. | list of 'str' | no |  |  |
| cert_organization_name | The Organization Name (O) of the certificate. | str | no |  |  |
| cert_organizational_unit_name | The Organizational Unit Name (OU) of the certificate. | str | no |  |  |
| cert_locality_name | The Locality Name (L) of the certificate. | str | no |  |  |
| cert_state_or_province_name | The State or Province Name (ST) of the certificate. | str | no |  |  |
| cert_country_name | The Country Name (C) of the certificate. | str | no |  |  |
| cert_key_usage | The key usage of the certificate. | list of 'str' | no |  | ["digitalSignature", "keyEncipherment"] |
| cert_key_usage_critical | Whether the key usage is critical. | bool | no |  | true |
| cert_extended_key_usage | The extended key usage of the certificate. | list of 'str' | no |  | ["serverAuth", "clientAuth"] |
| cert_extended_key_usage_critical | Whether the extended key usage is critical. | bool | no |  | true |
| cert_basic_constraints | The basic constraints of the certificate. | list of 'str' | no |  |  |
| cert_basic_constraints_critical | Whether the basic constraints are critical. | bool | no |  | true |
| cert_csr_tmp_path | The path to the CSR file to generate. On Linux, this defaults to `/tmp/cert.csr`. On Windows, this defaults to `C:\Windows\Temp\cert.csr`. | path | no |  | OS Specific |


## License
MIT

## Author and Project Information
Jim Tarpley @ Precision Aviation Group
<!-- END_ANSIBLE_DOCS -->
