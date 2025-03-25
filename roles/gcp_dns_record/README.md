<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: trippsc2.general.gcp_dns_record
Version: 2.9.2

This role sets a DNS record in Google Cloud DNS.


## Requirements

| Platform | Versions |
| -------- | -------- |
| GenericLinux | all |

## Role Arguments



### Entrypoint: main

GCP DNS Record

This role sets a DNS record in Google Cloud DNS.
|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| gcp_auth_kind | The type of credential used to authenticate with GCP. If set to `serviceaccount`, *gcp_service_account_file* or *gcp_service_account_contents* are required. If set to `accesstoken`, *gcp_access_token* is required. | str | yes |  |
| gcp_service_account_file | The path to the service account file. This is mutually exclusive with *gcp_service_account_contents*. If *gcp_auth_kind* is set to `serviceaccount`, this or *gcp_service_account_contents* are required. | path | no |  |
| gcp_service_account_contents | The contents of the service account file. This is mutually exclusive with *gcp_service_account_file*. If *gcp_auth_kind* is set to `serviceaccount`, this or *gcp_service_account_file* are required. | str | no |  |
| gcp_access_token | The OAuth2 access token which which to authenticate. If *gcp_auth_kind* is set to `accesstoken`, this is required. | str | no |  |
| gcp_project | The GCP project. | str | yes |  |
| gcp_scopes | The GCP scopes. | list of 'str' | no |  |
| gcp_dns_managed_zone_dns_name | The DNS name of the managed zone. | str | yes |  |
| gcp_dns_managed_zone_name | The name of the managed zone. | str | yes |  |
| gcp_dns_record_name | The name of the record. | str | yes |  |
| gcp_dns_record_type | The type of the DNS record. | str | yes |  |
| gcp_dns_record_ttl | The TTL of the DNS record in seconds. | int | no |  |
| gcp_dns_record_target | The target value of the DNS record. | list of 'str' | yes |  |

#### Choices for main > gcp_auth_kind

|Choice|
|---|
| application |
| machineaccount |
| serviceaccount |
| accesstoken |

#### Choices for main > gcp_dns_record_type

|Choice|
|---|
| A |
| AAAA |
| CAA |
| CNAME |
| DNSKEY |
| DS |
| IPSECVPNKEY |
| MX |
| NAPTR |
| NS |
| PTR |
| SOA |
| SPF |
| SRV |
| SSHFP |
| TLSA |
| TXT |



## Dependencies
None.

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing role: trippsc2.general.gcp_dns_record
      ansible.builtin.import_role:
        name: trippsc2.general.gcp_dns_record
      vars:
        gcp_auth_kind: # required, type: str
        gcp_project: # required, type: str
        gcp_dns_managed_zone_dns_name: # required, type: str
        gcp_dns_managed_zone_name: # required, type: str
        gcp_dns_record_name: # required, type: str
        gcp_dns_record_type: # required, type: str
        gcp_dns_record_target: # required, type: list of 'str'
```

## License

MIT

## Author and Project Information
Jim Tarpley (@trippsc2)

<!-- END_ANSIBLE_DOCS -->
