# Changelog

All notable changes to this project will be documented in this file.

## [2.10.1] - 2025-06-10

### Collection

- Changed repository URL to use GitHub Organization.

## [2.10.0] - 2025-05-15

### Collection

- Removed *rotate_linux_password* role.

### Role - generate_csr

- Changed OS validation.

### Role - self_signed_certificate

- Changed OS validation.

## [2.9.2] - 2025-03-25

### Role - acme_dns_certificate

- Fixed bug regarding intermediate CA certificate to variable.

## [2.9.1] - 2025-03-25

### Role - acme_dns_certificate

- Changed `cert_acme_dns_role` and `cert_acme_dns_custom_role` to match other similar roles by renaming to `cert_acme_dns_type` and `cert_acme_dns_role` and simplifying pre-filled options.

## [2.9.0] - 2025-03-24

### Collection

- *gcp_dns_record* role added.
- *acme_dns_certificate* role added.

## [2.8.0] - 2025-02-20

### Role - generate_csr

- Added `cert_private_key_passphrase` option to allow the private key to be encrypted.
- Added support for Nobara Linux to allow for local testing of the role in certain contexts.
- Removed all support for CSR to file.  If this is needed, copy the contents of `cert_csr_content` to a file using a task.

### Role - self_signed_certificate

- Added `cert_private_key_passphrase` option to allow the private key to be encrypted.
- Added support for Nobara Linux to allow for local testing of the role in certain contexts.
- Removed all support for CSR to file.  If this is needed, copy the contents of `cert_csr_content` to a file using a task.

## [2.7.0] - 2025-02-18

### Role - generate_csr

- Restructured role to make writing the CSR and private key to files optional.

### Role - self_signed_certificate

- Restructured role to compliment changes in *generate_csr* role and to make saving the certificate to a file optional.

## [2.6.5] - 2025-02-13

### Module Plugin - combine_certificates

- Reverted changing documentation from .py file to .yml file because ansible-lint does not parse it correctly yet.

### Test Plugin - tz

- Reverted changing documentation from .py file to .yml file because ansible-lint does not parse it correctly yet.

## [2.6.4] - 2025-02-09

### Module Plugin - combine_certificates

- Made several code quality and style changes to the module that were recommended by the Ansible sanity tests.

## [2.6.3] - 2025-01-08

### Collection

- Added Changelog.
- Updated collection README documentation.

## [2.6.2] - 2024-10-22

### Role - generate_csr

- Added `os_family` subset to fact gathering task.

### Role - rotate_linux_password

- Removed `os_family` subset from fact gathering task.

## [2.6.1] - 2024-09-24

### Role - generate_csr

- Removed `become` option from Windows tasks.

## [2.6.0] - 2024-09-24

### Collection

- *tz* test plugin added.

## [2.5.1] - 2024-09-06

### Role - rotate_linux_password

- Added `no_log` option to `rotate_new_password` variable.

## [2.5.0] - 2024-09-06

### Collection

- *rotate_linux_password* role added.

### Role - generate_csr

- Corrected Ubuntu versions listed in the role metadata.

### Role - self_signed_certificate

- Corrected Ubuntu versions listed in the role metadata.

## [2.4.1] - 2024-08-09

### Collection

- Minimum Ansible version changed from `2.14` to `2.15` due to EOL status.

## [2.4.0] - 2024-07-26

### Role - generate_csr

- Removed defaults for the `cert_private_key_path` and `cert_certificate_path` variables and made them required to prevent unexpected behavior.

### Role - self_signed_certificate

- Removed defaults for the `cert_private_key_path` and `cert_certificate_path` variables and made them required to prevent unexpected behavior.

## [2.3.6] - 2024-07-11

### Role - generate_csr

- Updated documentation and role metadata for readability.
- Added validation where possible.

### Role - self_signed_certificate

- Updated documentation and role metadata for readability.
- Added validation where possible.

## [2.3.5] - 2024-07-08

### Role - generate_csr

- Added step to gather facts regarding the OS family.

### Role - self_signed_certificate

- Added step to gather facts regarding the OS family.
- Added step to add the `cert_private_key_owner` user to the `ssl-cert` group on Debian-based machines.

## [2.3.3] - 2024-06-30

### Role - generate_csr

- Changed references to Red Hat Enterprise Linux (RHEL) to more accurately reference Enterprise Linux (EL) to convey the intention to support derivatives (Rocky/AlmaLinux/etc.)

### Role - self_signed_certificate

- Changed references to Red Hat Enterprise Linux (RHEL) to more accurately reference Enterprise Linux (EL) to convey the intention to support derivatives (Rocky/AlmaLinux/etc.)

## [2.3.2] - 2024-06-29

### Role - generate_csr

- Added `allow_duplicates` to the role metadata.
- Role refactored to not make use of `ignore_errors` option and instead use `rescue` block.

## [2.3.1] - 2024-06-27

### Role - generate_csr

- Role refactored to not make use of `ignore_errors` option when checking for existing certificate.

## [2.3.0] - 2024-06-27

### Collection

- *win_combine_certificates* module plugin removed.  Moved to **trippsc2.windows** collection as *trippsc2.windows.win_combine_certificates* module plugin.
- *win_package_provider* module plugin removed.  Moved to **trippsc2.windows** collection as *trippsc2.windows.win_package_provider* module plugin.

## [2.2.0] - 2024-06-21

### Collection

- *self_signed_certificate* role added.

## [2.1.2] - 2024-06-20

### Role - generate_csr

- Updated documentation and role metadata for readability.

## [2.1.1] - 2024-06-11

### Collection

- Minimum Ansible version changed from `2.11` to `2.14` due to align with EOL status.

### Role - generate_csr

- Added support for Debian 11 and 12, EL 9, and Ubuntu 20.04, 22.04, and 24.04 to the role metadata.

## [2.1.0] - 2024-06-11

### Collection

- Added dependency reference to **ansible.windows** collection.
- Added dependency reference to **community.crypto** collection.
- *win_package_provider* module plugin added.

## [2.0.0] - 2024-06-10

### Collection

- *generate_csr* role added.

## [1.0.0] - 2024-06-10

### Collection

- Initial release.
- *combine_certificates* module plugin added.
- *win_combine_certificates* module plugin added.
