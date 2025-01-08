#! /bin/bash

cd ./roles/generate_csr

aar-doc . markdown

cd ../rotate_linux_password

aar-doc . markdown

cd ../self_signed_certificate

aar-doc . markdown
