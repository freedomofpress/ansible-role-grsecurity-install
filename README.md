# ansible-role-grsecurity-install

Installs Debian packages for [grsecurity]-patched Linux kernels.
Requires packages built with the [grsecurity-build] role.

## Requirements

### Platforms
Only Debian and Ubuntu are supported, due to the use of deb packages.


In the future, these roles may be broken out into separate repositories. Feel free to
[open an issue](https://github.com/freedomofpress/ansible-role-grsecurity/issues)
to discuss how such a change might affect your workflow.

## Role variables

The install role expects a .deb package filepath on the Ansible controller, the same
file that was created by the build role, and will install that package on the target host.

```yaml
# The filepath of the .deb package on the Ansible controller. This var is required,
# but can't be known ahead of time, so you must specify it manually. The role will
# fail if this var is not updated. Use the build role to create a package first.
grsecurity_install_deb_package: ''

# Secondary list var to support multiple deb packages, e.g. image, headers, src.
# This list will be concatenated with the scalar var above when generating the
# the list of deb packages to be installed.
grsecurity_install_deb_packages: []

# For easier console recovery and debugging, the GRUB timeout value (default: 5)
# can be overridden here. Without a lengthier timeout, it can be very difficult
# to get into the GRUB menu and select a working kernel to boot. Debian uses 5
# by default, which we're replicating here for consistency and predictability.
grsecurity_install_grub_timeout: 5

# paxctld is a better alternative than paxctl for maintaining the PaX flags on binaries.
# The paxctld role isn't a dependency yet, so assume the paxctl approach is safest.
# If you're using the paxctld role, set this to false.
grsecurity_install_set_paxctl_flags: true

# Location where the .deb files will be copied on the target host, prior to install.
grsecurity_install_download_dir: /usr/local/src

# The role will skip installation if the kernel version, e.g. "4.4.2-grsec",
# of the deb package matches that of the target host, provided the checksum
# for the deb file is the same. If you want to reinstall the same kernel version,
# for example while developing a new kernel config, set this to true.
grsecurity_install_force_install: false

# If the target host is remote, assume that rebooting is desired, but don't
# reboot if we're installing on localhost.
grsecurity_install_reboot: "{{ false if ansible_connection == 'local' else true }}"
```
## Examples

```
- name: Install a grsecurity-patched Linux kernel deb package.
  hosts: grsecurity_hosts
  roles:
    - role: freedomofpress.grsecurity-install
```

## Further reading

* [Official grsecurity website](https://grsecurity.net/)
* [Grsecurity/PaX wikibook](https://en.wikibooks.org/wiki/Grsecurity/Appendix/Grsecurity_and_PaX_Configuration_Options)
* [Linux Kernel in a Nutshell](http://www.kroah.com/lkn/)

[Freedom of the Press Foundation]: https://freedom.press
[SecureDrop]: https://securedrop.org
[grsecurity]: https://grsecurity.net/
[grsecurity subscription]: https://grsecurity.net/business_support.php
[grsecurity-build]: https://github.com/freedomofpress/ansible-role-grsecurity-build
