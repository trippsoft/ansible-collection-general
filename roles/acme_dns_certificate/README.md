<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: trippsc2.general.acme_dns_certificate
Version: 2.10.2

This role generates an ACME TLS certificate.

The role depends on the `trippsc2.general.generate_csr` role to generate a private key and CSR.

The role depends on another role to set a DNS TXT record for the ACME challenge.

The role does the following:
  - Runs the `trippsc2.general.generate_csr` role to generate a private key and CSR, if needed.
  - If the private key and CSR are generated, the role issues a dns-01 challenge to the ACME server.
  - The DNS role is responsible for setting the DNS TXT record for the ACME challenge.
  - Once the DNS record is set, the role will request the certificate from the ACME server and store it in the `cert_certificate_content` variable.
  - Optionally, the role will save the certificate to a file.



## Requirements

| Platform | Versions |
| -------- | -------- |
| Debian | bookworm |
| EL | 9, 8 |
| Ubuntu | noble, jammy |
| Windows | all |

## Role Arguments



### Entrypoint: main

ACME Certificate - DNS Challenge

This role generates an ACME TLS certificate.

The role depends on the `trippsc2.general.generate_csr` role to generate a private key and CSR.

The role depends on another role to set a DNS TXT record for the ACME challenge.

The role does the following:
  - Runs the `trippsc2.general.generate_csr` role to generate a private key and CSR, if needed.
  - If the private key and CSR are generated, the role issues a dns-01 challenge to the ACME server.
  - The DNS role is responsible for setting the DNS TXT record for the ACME challenge.
  - Once the DNS record is set, the role will request the certificate from the ACME server and store it in the `cert_certificate_content` variable.
  - Optionally, the role will save the certificate to a file.


|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| cert_acme_account_key_content | The contents of the account key. This is used to identify yourself to the ACME server when revoking the certificate, as opposed to the private key of the certificate. | str | yes |  |
| cert_acme_account_key_passphrase | The passphrase for the account key. If not provided, the account key is assumed to be unencrypted. | str | no |  |
| cert_acme_account_email | The email address to use for the ACME account. | str | yes |  |
| cert_acme_account_uri | The URI of the ACME account. This is used to revoke the certificate. | str | no |  |
| cert_acme_directory | The ACME directory URL. | str | yes |  |
| cert_acme_version | The ACME version to use. | int | no | 2 |
| cert_acme_terms_agreed | Whether the terms of service should be agreed to. | bool | no |  |
| cert_acme_intermediate_certificate_to_file | Whether to save the intermediate certificate to a file. | bool | no | True |
| cert_acme_intermediate_certificate_to_variable | Whether to store the intermediate certificate in a variable. If set to `true`, the intermediate certificate will be stored in the `cert_acme_intermediate_certificate_content` variable. | bool | no | False |
| cert_acme_intermediate_certificate_path | The path to save the intermediate certificate file. If *cert_acme_intermediate_certificate_to_file* is `true`, this is required. | path | no |  |
| cert_acme_intermediate_certificate_owner | The owner of the certificate on Linux systems. On Windows systems, this is ignored. | str | no | root |
| cert_acme_intermediate_certificate_group | The group of the certificate on Linux systems. On Windows systems, this is ignored. | str | no | root |
| cert_acme_intermediate_certificate_mode | The mode of the certificate on Linux systems. On Windows systems, this is ignored. | str | no | 0644 |
| cert_acme_validate_certs | Whether to validate the ACME server certificates. | bool | no | True |
| cert_acme_dns_type | The role to use to set the DNS TXT record for the ACME challenge. If set to `custom`, the `cert_acme_dns_role` variable must be defined. | str | yes |  |
| cert_acme_dns_role | The custom role to use to set the DNS TXT record for the ACME challenge. This is required if *cert_acme_dns_type* is set to `custom`. | str | no |  |
| cert_certificate_to_file | Whether to generate the certificate to a file. If set to `true`, the certificate will be stored at the path specified in the `cert_certificate_path` variable. | bool | no | True |
| cert_certificate_to_variable | Whether to store the certificate in a variable. If set to `true`, the certificate will be stored in the `cert_certificate_content` variable. | bool | no | False |
| cert_certificate_path | The path to the certificate file to generate. If *cert_certificate_to_file* is `true`, this is required. | path | no |  |
| cert_certificate_owner | The owner of the certificate on Linux systems. On Windows systems, this is ignored. | str | no | root |
| cert_certificate_group | The group of the certificate on Linux systems. On Windows systems, this is ignored. | str | no | root |
| cert_certificate_mode | The mode of the certificate on Linux systems. On Windows systems, this is ignored. | str | no | 0644 |

#### Choices for main > cert_acme_version

|Choice|
|---|
| 1 |
| 2 |

#### Choices for main > cert_acme_dns_type

|Choice|
|---|
| gcp |
| custom |



## Dependencies
- {'role': 'trippsc2.general.generate_csr'}

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: trippsc2.general.acme_dns_certificate
      ansible.builtin.import_role:
        name: trippsc2.general.acme_dns_certificate
      vars:
        cert_acme_account_key_content: # required, type: str
        cert_acme_account_email: # required, type: str
        cert_acme_directory: # required, type: str
        cert_acme_dns_type: # required, type: str
```

## License

MIT

## Author and Project Information
Jim Tarpley (@trippsc2)

<!-- END_ANSIBLE_DOCS -->
