
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError
from ansible.module_utils.six import raise_from

try:
    from pytz import timezone
    from pytz.exceptions import UnknownTimeZoneError
except ImportError as import_exception:
    LIBRARY_MISSING_EXCEPTION = import_exception
else:
    LIBRARY_MISSING_EXCEPTION = None


def tz(value) -> bool:
    """
    Whether the timezone name is valid.

    Args:
        value: The timezone name to validate.

    Returns:
        bool: Whether the timezone name is valid.
    """

    if LIBRARY_MISSING_EXCEPTION is not None:
        raise_from(
            AnsibleError('Python package pytz must be installed to use this test.'),
            LIBRARY_MISSING_EXCEPTION
        )

    try:
        timezone(value)
    except UnknownTimeZoneError:
        return False
    except Exception as e:
        raise_from(AnsibleError('An error occurred while validating the timezone name.'), e)

    return True


class TestModule:
    def tests(self):
        return {
            'tz': tz
        }
