#! /bin/bash

cd ./roles/generate_csr

aar_doc . markdown

cd ../rotate_linux_password

aar_doc . markdown

cd ../self_signed_certificate

aar_doc . markdown
