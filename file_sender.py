from pathlib import Path
from paramiko import SSHClient, ed25519key, AutoAddPolicy
from scp import SCPClient
from config import Config


def file_Sender(my_file, distant_path):
    hostname = Config.ssh_hostname
    user = Config.ssh_user
    ssh_key = Config.ssh_key
    private_key = ed25519key.Ed25519Key.from_private_key_file(ssh_key)
    with SSHClient() as client:
        client.set_missing_host_key_policy(AutoAddPolicy)
        print('---------- SSH connexion started----------')
        client.connect(hostname, username=user, pkey=private_key)
        with SCPClient(client.get_transport()) as scp:
            scp.put(my_file, distant_path)
    print('---------- SSH connexion closed ----------')

if __name__ == '__main__':

    my_file = Config.temp_file
    distant_path = '/home/ubuntu/temp.json'
    file_Sender(my_file, distant_path)
