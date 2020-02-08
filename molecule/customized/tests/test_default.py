import json
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
    binary = host.file("/opt/rclone/rclone")

    assert binary.exists
    assert binary.is_file
    assert binary.user == "root"
    assert binary.group == "root"
    assert binary.mode == 0o755


def test_man(host):
    f = host.file("/usr/share/man/man1/rclone.1")

    assert f.exists
    assert f.is_file
    assert f.mode == 0o644


def test_versions(host):
    version = 'v1.50.0'
    assert host.check_output("/opt/rclone/rclone version").splitlines(
            )[0].split()[1] == version


def test_config(host):
    conf = host.file("/root/.local/rclone/rclone.conf")

    content = ("[dropbox]\n"
               "type = dropbox\n"
               "app_key = \n"
               "app_secret = \n"
               "token = "
               "{\"access_token\":\"secret-token-\","
               "\"token_type\":\"bearer\","
               "\"expiry\":\"0001-01-01T00:00:00Z\"}\n\n"
               "[encrypted-media]\n"
               "type = crypt\n"
               "remote = google-drive:media\n"
               "filename_encryption = standard\n"
               "password = <PASSWORD>\n"
               "password2 = <PASSWORD2>\n\n")

    assert conf.exists
    assert conf.is_file
    assert conf.mode == 0o600
    assert conf.content_string == content

    dump = host.check_output((
        "/opt/rclone/rclone "
        "--config "
        "/root/.local/rclone/rclone.conf "
        "config "
        "dump"
    ))

    json_conf = json.loads(dump)

    assert json_conf['dropbox']['type'] == "dropbox"
