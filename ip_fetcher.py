import socket
import os

host_names = []
filename_hostnames = "websites.txt"
filename_hosts = "hosts"


def get_ip(host_name: str) -> str:
    return str(socket.gethostbyname(host_name))


def fetch_websites():
    with open(filename_hostnames, "rt") as f:
        for line in f.readlines():
            line = line.split("#",1)[0].strip()
            if line == "":
                continue
            host_names.append(line)

    print()
    print(f'Please enter your websites into the file {filename_hostnames}.')
    print()
    print(f'You can add the output of this file to the following file:')
    print(' C:\\Windows\\System32\\drivers\\etc\\hosts\\')
    print()
    print(f'The output will also be saved right next to this program file into the file "{filename_hosts}"')
    print()
    with open(filename_hosts, "wt") as f:
        for host_name in host_names:
            line = get_ip(host_name).ljust(15) + " "
            line += host_name
            f.write(line)
            f.write(os.linesep)
            print(line)

if __name__ = "__main__":
    fetch_websites()