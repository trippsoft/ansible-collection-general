# Ansible Collection: trippsc2.general

This collection contains general purpose Ansible plugins.

## Content

### Module plugins

- combine_certificates - Combine multiple certificates into a single file.

### Test plugins

- tz - Validates Linux timezone names.

### Roles

- [acme_dns_certificate](roles/acme_dns_certificate/README.md) - This role generates an ACME TLS certificate.
- [gcp_dns_record](roles/gcp_dns_record/README.md) - This role sets a DNS record in Google Cloud DNS.
- [generate_csr](roles/generate_csr/README.md) - This role generates a Certificate Signing Request (CSR) for a Linux or Windows machine, if an existing certificate doesn't exist or needs renewal.
- [rotate_linux_password](roles/rotate_linux_password/README.md) - This role rotates a Linux user password.
- [self_signed_certificate](roles/self_signed_certificate/README.md) - This role generates a self-signed TLS certificate.
