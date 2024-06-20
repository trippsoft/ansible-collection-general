<!-- BEGIN_ANSIBLE_DOCS -->

# Ansible Role: trippsc2.general.generate_csr
Version: 2.1.2

This role generates a Certificate Signing Request (CSR) for a Linux or Windows machine, if an existing certificate doesn't exist or needs renewal.

## Requirements

| Platform | Versions |
| -------- | -------- |
| Debian | <ul><li>bullseye</li><li>bookworm</li></ul> |
| EL | <ul><li>8</li><li>9</li></ul> |
| Ubuntu | <ul><li>focal</li><li>hirsute</li><li>impish</li></ul> |
| Windows | <ul><li>2019</li><li>2022</li></ul> |

## Dependencies

| Collection |
| ---------- |
| ansible.windows |
| community.crypto |

## Role Arguments
|Option|Description|Type|Required|Choices|Default|
|---|---|---|---|---|---|
| cert_force_regenerate | <p>Whether to force regeneration of the CSR, even if the certificate is not near expiration.</p><p>If `true`, the role will not be idempotent.</p> | bool | no |  | false |
| cert_certifcate_path | <p>The path to the certificate file to generate.</p><p>On Debian-based Linux, this defaults to `/etc/ssl/certs/cert.crt`.</p><p>On Red Hat-based Linux, this defaults to `/etc/pki/tls/certs/cert.crt`.</p><p>On Windows, this defaults to `C:\Windows\Temp\cert.crt`.</p> | path | no |  | OS Specific |
| cert_regenerate_days | <p>The number of days before the certificate expiration to regenerate the CSR.</p> | int | no |  | 30 |
| cert_private_key_path | <p>The path to the private key file to generate.</p><p>On Debian-based Linux, this defaults to `/etc/ssl/private/cert.key`.</p><p>On Red Hat-based Linux, this defaults to `/etc/pki/tls/private/cert.key`.</p><p>On Windows, this defaults to `C:\Windows\Temp\cert.key`.</p> | path | no |  | OS Specific |
| cert_private_key_owner | <p>The owner of the private key on Linux systems.</p> | str | no |  | root |
| cert_private_key_group | <p>The group of the private key on Linux systems.</p> | str | no |  | root |
| cert_private_key_mode | <p>The mode of the private key on Linux systems.</p> | str | no |  | 0600 |
| cert_private_key_type | <p>The type of private key to generate.</p> | str | no | <ul><li>DSA</li><li>ECC</li><li>Ed25519</li><li>Ed448</li><li>RSA</li><li>X25519</li><li>X448</li></ul> | RSA |
| cert_private_key_size | <p>The size of the private key to generate.</p> | int | no |  | 2048 |
| cert_backup_replaced_private_key | <p>Whether to backup the replaced private key.</p> | bool | no |  | true |
| cert_common_name | <p>The Common Name (CN) of the certificate.</p> | str | no |  | {{ inventory_hostname }} |
| cert_subject_alternative_names | <p>The Subject Alternative Names (SANs) of the certificate.</p><p>DNS names should be prefixed with `DNS:` and IP addresses should be prefixed with `IP:`.</p> | list of 'str' | no |  |  |
| cert_organization_name | <p>The Organization Name (O) of the certificate.</p> | str | no |  |  |
| cert_organizational_unit_name | <p>The Organizational Unit Name (OU) of the certificate.</p> | str | no |  |  |
| cert_locality_name | <p>The Locality Name (L) of the certificate.</p> | str | no |  |  |
| cert_state_or_province_name | <p>The State or Province Name (ST) of the certificate.</p> | str | no |  |  |
| cert_country_name | <p>The Country Name (C) of the certificate.</p> | str | no |  |  |
| cert_key_usage | <p>The key usage of the certificate.</p> | list of 'str' | no |  | ["digitalSignature", "keyEncipherment"] |
| cert_key_usage_critical | <p>Whether the key usage is critical.</p> | bool | no |  | true |
| cert_extended_key_usage | <p>The extended key usage of the certificate.</p> | list of 'str' | no |  | ["serverAuth", "clientAuth"] |
| cert_extended_key_usage_critical | <p>Whether the extended key usage is critical.</p> | bool | no |  | true |
| cert_basic_constraints | <p>The basic constraints of the certificate.</p> | list of 'str' | no |  |  |
| cert_basic_constraints_critical | <p>Whether the basic constraints are critical.</p> | bool | no |  | true |
| cert_csr_tmp_path | <p>The path to the CSR file to generate.</p><p>On Linux, this defaults to `/tmp/cert.csr`.</p><p>On Windows, this defaults to `C:\Windows\Temp\cert.csr`.</p> | path | no |  | OS Specific |


## License
MIT

## Author and Project Information
Jim Tarpley
<!-- END_ANSIBLE_DOCS -->
