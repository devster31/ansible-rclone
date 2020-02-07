rclone
=========

[![molecule test](https://github.com/devster31/ansible-rclone/workflows/molecule%20test/badge.svg)](https://github.com/devster31/ansible-rclone/actions)

This role installs, updates, and configures [`rclone`](https://github.com/rclone/rclone).

Requirements
------------

None.

Usage
-----

1. Clone this repo into your local roles-directory or install via `ansible-galaxy install stefangweichinger.rclone`.
2. Add role to the hosts you want rclone installed to.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml` and `vars/*.yml`):

```yaml
rclone__enabled: yes
```

This variable toggles installation or removal of the role.

```yaml
rclone__version: latest
```

The version of rclone to install. By default it's set to `latest`. This recovers the latest version and installs it.
You can specify a version (including the `v` in front of the number), set this variable to `beta` or `latest_github`
which queries GitHub for the latest available release.

```yaml
rclone__go_arch_map:
  i386: "386"
  x86_64: "amd64"
  aarch64: "arm64"
  armv7l: "arm"
  armv6l: "arm"

rclone__go_arch: "{{ rclone__go_arch_map[ansible_architecture] | default(ansible_architecture) }}"
```

These variables convert the architecture dectedted by `ansible` into a compatible
`go_arch` variable used by [`rclone`](https://github.com/rclone/rclone) in the release name.

```yaml
rclone__binary: /usr/local/bin/rclone
rclone__dirname_mode: ugo+x
rclone__binary_mode: 0755
rclone__user: root
rclone__group: root
```

This group of variables sets the path for the [`rclone`](https://github.com/rclone/rclone) binary, the directory mode,
and user/group owners.

```yaml
rclone__install_man: no
# without trailing slash
rclone__man_path: /usr/local/share/man/man1
```

These variables control installation of `manpages` and their location.

```yaml
rclone__configure: no
rclone__configs: []
```

These variables control whether to configure [`rclone`](https://github.com/rclone/rclone) or not.
Example:

```yaml
rclone__configure: yes
rclone__configs:
  - user: root
    path: /root/.local/rclone/rclone.conf
    blocks:
      dropbox:
        type: dropbox
        app_key: ~
        app_secret: ~
        token: '{"access_token":"secret-token-","token_type":"bearer","expiry":"0001-01-01T00:00:00Z"}'
```

Within configs `user` controls ownership of the `path`.
`blocks` generate `ini` configuration blocks.
The previous example generates:

```ini
[dropbox]
type = dropbox
app_key =
app_secret =
token = {"access_token":"secret-token-","token_type":"bearer","expiry":"0001-01-01T00:00:00Z"}

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

Tests are run using [molecule](https://molecule.readthedocs.io/en/latest/index.html)

Currently there are three scenarios defined:

* default: runs installation with default variables
* customized: runs installation with `manpages` and configures [`rclone`](https://github.com/rclone/rclone)
* remove: tests removal of the role