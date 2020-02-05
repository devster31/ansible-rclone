rclone
=========

This role installs, updates, and configures [rclone](https://github.com/ncw/rclone).

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should
be mentioned here. For instance, if the role uses the EC2 module, it may be a
good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including
any variables that are in defaults/main.yml, vars/main.yml, and any variables
that can/should be set via parameters to the role. Any variables that are read
from other roles and/or the global scope (ie. hostvars, group vars, etc.) should
be mentioned here as well.

```yaml
---
# defaults file for rclone
rclone__enabled: yes
rclone__version: latest

rclone__go_arch_map:
  i386: "386"
  x86_64: "amd64"
  aarch64: "arm64"
  armv7l: "arm"
  armv6l: "arm"

rclone__go_arch: "{{ rclone__go_arch_map[ansible_architecture] | default(ansible_architecture) }}"

rclone__binary: /usr/local/bin/rclone
rclone__dirname_mode: ugo+x
rclone__binary_mode: 0755
rclone__user: root
rclone__group: root
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
---
- hosts: all
  roles:
    - role: rclone
...
```

License
-------

GPLv2

Tests
-----

[molecule](https://molecule.readthedocs.io/en/latest/index.html)