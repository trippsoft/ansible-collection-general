#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r"""
module: combine_certificates
version_added: 1.0.0
author:
  - Jim Tarpley
short_description: Combine multiple certificates into a single file.
description:
  - Combines multiple certificates into a single file in order.
attributes:
  check_mode:
    support: full
    details:
      - This module supports check mode.
options:
  certificates:
    description:
      - List of certificates to combine.
    required: true
    type: list(str)
  path:
    description:
      - Path to the combined certificate file.
    required: true
    type: str
extends_documentation_fragment:
  - ansible.builtin.files
"""

EXAMPLES = r"""
"""

RETURN = r"""
"""

import errno
import os

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native


def main():
    module = AnsibleModule(
        argument_spec=dict(
            certificates=dict(type='list', elements='path', required=True),
            path=dict(type='path', required=True)
        ),
        add_file_common_args=True,
        supports_check_mode=True
    )

    owner = module.params.get('owner', None)
    group = module.params.get('group', None)
    mode = module.params.get('mode', None)

    changed = False

    expected_content = ''

    for certificate in module.params['certificates']:
        if expected_content != '':
            expected_content += '\n'
        
        try:
            with open(certificate, 'r') as file:
                expected_content += file.read()
        except (IOError, OSError) as e:
            if e.errno == errno.ENOENT:
                msg = "file not found: %s" % certificate
            elif e.errno == errno.EACCES:
                msg = "file is not readable: %s" % certificate
            elif e.errno == errno.EISDIR:
                msg = "source is a directory and must be a file: %s" % certificate
            else:
                msg = "unable to read file: %s" % to_native(e, errors='surrogate_then_replace')

            module.fail_json(msg)

    path = module.params['path']

    if os.path.exists(path):
        
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

            module.fail_json(msg)
    else:
        actual_content = None

    if actual_content is None or expected_content != actual_content:
        
        changed = True

        if not module.check_mode:
            
            try:
                with open(path, 'w') as file:
                    file.write(expected_content)
            except (IOError, OSError) as e:
                if e.errno == errno.EACCES:
                    msg = "file is not writable: %s" % path
                else:
                    msg = "unable to write file: %s" % to_native(e, errors='surrogate_then_replace')

                module.fail_json(msg)

    changed = module.set_owner_if_different(
        path,
        owner,
        changed
    )

    changed = module.set_group_if_different(
        path,
        group,
        changed
    )

    changed = module.set_mode_if_different(
        path,
        mode,
        changed
    )        

    module.exit_json(changed=changed)


if __name__ == '__main__':
    main()
