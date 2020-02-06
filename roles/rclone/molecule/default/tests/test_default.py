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
