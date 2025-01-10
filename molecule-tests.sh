#! /bin/bash

set -e

MOLECULE_BOX="rocky9_cis" molecule test -s combine_certificates
MOLECULE_BOX="debian12_base" molecule test -s combine_certificates
MOLECULE_BOX="fedora41_base" molecule test -s combine_certificates
MOLECULE_BOX="ubuntu2404_base" molecule test -s combine_certificates

MOLECULE_BOX="rocky8_cis" molecule test -s combine_certificates

MOLECULE_BOX="debian11_base" molecule test -s combine_certificates

MOLECULE_BOX="ubuntu2204_base" molecule test -s combine_certificates
MOLECULE_BOX="ubuntu2004_base" molecule test -s combine_certificates

molecule test -s tz
