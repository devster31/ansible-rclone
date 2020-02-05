import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_fact(host):
    fact = host.file("/etc/ansible/facts.d/rclone.fact")

    assert fact.exists
    assert fact.is_file


def test_binary(host):
    binary = host.file("/usr/local/bin/rclone")

    assert binary.exists
    assert binary.is_file
    assert binary.user == "root"
    assert binary.group == "root"
    assert binary.mode == 0o755


def test_man(host):
    f = host.file("/usr/local/share/man/man1/rclone.1")

    assert f.exists
    assert f.is_file
    assert f.mode == 0o644

# todo: pointless test as local facts runs the same piece of code
# def test_versions(host):
#     version = host.ansible("setup")["ansible_facts"][
#         "ansible_local"]["rclone"]["version"]
#     assert host.check_output("rclone version").splitlines(
#             )[0].split()[1] == version
