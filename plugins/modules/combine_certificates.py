#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r"""
module: combine_certificates
version_added: 1.0.0
author:
  - Jim Tarpley (@trippsc2)
short_description: Combine multiple certificates into a single file.
description:
  - Combines multiple certificates into a single file in order.
attributes:
  check_mode:
    support: full
    description:
      - This module supports check mode.
options:
  certificates:
    type: list
    required: true
    elements: path
    description:
      - List of certificates to combine.
  path:
    type: path
    required: true
    description:
      - Path to the combined certificate file.
extends_documentation_fragment:
  - ansible.builtin.files
"""

EXAMPLES = r"""
- name: Combine certificates
  trippsc2.general.combine_certificates:
    certificates:
      - /path/to/cert1.pem
      - /path/to/cert2.pem
      - /path/to/cert3.pem
    path: /path/to/combined.pem
    owner: root
    group: root
    mode: '0600'
"""

RETURN = r"""
"""

import errno
import os

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native

from typing import List, Optional


def main() -> None:
    module: AnsibleModule = AnsibleModule(
        argument_spec=dict(
            certificates=dict(type='list', elements='path', required=True),
            path=dict(type='path', required=True)
        ),
        add_file_common_args=True,
        supports_check_mode=True
    )

    path: str = module.params['path']
    owner: Optional[str] = module.params.get('owner', None)
    group: Optional[str] = module.params.get('group', None)
    mode: Optional[str] = module.params.get('mode', None)
    certificates: List[str] = module.params['certificates']

    changed: bool = False

    expected_content: str = ''

    for certificate in certificates:
        if expected_content != '':
            expected_content += '\n'

        try:
            with open(certificate, 'r') as file:
                expected_content += file.read()
        except (IOError, OSError) as e:
            if e.errno == errno.ENOENT:
                msg: str = "file not found: %s" % certificate
            elif e.errno == errno.EACCES:
                msg: str = "file is not readable: %s" % certificate
            elif e.errno == errno.EISDIR:
                msg: str = "source is a directory and must be a file: %s" % certificate
            else:
                msg: str = "unable to read file: %s" % to_native(e, errors='surrogate_then_replace')

            module.fail_json(msg)

    actual_content: Optional[str] = None

    if os.path.exists(path):

        msg: Optional[str] = None

        try:
            with open(path, 'r') as file:
                actual_content = file.read()
        except (IOError, OSError) as e:
            if e.errno == errno.EACCES:
                msg = "file is not readable: %s" % path
            elif e.errno == errno.EISDIR:
                msg = "source is a directory and must be a file: %s" % path
            else:
                msg = "unable to read file: %s" % to_native(e, errors='surrogate_then_replace')

        if msg is not None:
            module.fail_json(msg)

    if actual_content is None or expected_content != actual_content:

        changed = True

        if not module.check_mode:

            msg: Optional[str] = None

            try:
                with open(path, 'w') as file:
                    file.write(expected_content)
            except (IOError, OSError) as e:
                if e.errno == errno.EACCES:
                    msg = "file is not writable: %s" % path
                else:
                    msg = "unable to write file: %s" % to_native(e, errors='surrogate_then_replace')

            if msg is not None:
                module.fail_json(msg)

    changed = module.set_owner_if_different(path, owner, changed)
    changed = module.set_group_if_different(path, group, changed)
    changed = module.set_mode_if_different(path, mode, changed)

    module.exit_json(changed=changed)


if __name__ == '__main__':
    main()
