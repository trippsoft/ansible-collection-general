#! /bin/bash

cd ./roles/acme_dns_certificate

aar-doc . markdown

cd ../gcp_dns_record

aar-doc . markdown

cd ../generate_csr

aar-doc . markdown

cd ../self_signed_certificate

aar-doc . markdown
