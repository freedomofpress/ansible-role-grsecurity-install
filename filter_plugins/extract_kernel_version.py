import os
import re

from ansible import errors


def extract_kernel_version(deb_package):
    """
    Read filename for linux-image Debian package and return only
    the kernel version it would install, e.g. "4.4.4-grsec".
    """

    # Convert to basename in case the filter
    # call was not prefixed with '|basename'.
    deb_package = os.path.basename(deb_package)
    try:
        reg_pattern = "^.*-image-([\d.]+-grsec[A-Za-z0-9\-\.]*)_.*$"
        results = re.findall(r'{}'.format(reg_pattern), deb_package)[0]
    except IndexError:
        msg = ("Could not determine desired kernel version in '{}', make sure"
               " it matches the regular expression '{}'"
               ).format(deb_package, reg_pattern)
        raise errors.AnsibleFilterError(msg)

    return results


class FilterModule(object):
    def filters(self):
        return {
            'extract_kernel_version': extract_kernel_version
        }
