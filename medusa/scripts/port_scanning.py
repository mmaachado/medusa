#!/bin/usr/python
#
# Filename: port_scanning.py
# Description: Powerfull tool to check every open port
# Author: marques <uniqueduckinbox at duck.com>
# URL: https://github.com/mmaachado/medusa
# Keywords: Medusa Offensive Security PenTest Red Team Port Scan
# Compatibility: python-version >= 3.12.5
#
# ----------------------------
#
# Commentary:
#
# this is a simple yet powerfull port scanner.
#
# ----------------------------
#
# This program is a free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with your GNU/Linux distribution.  If not, see <https://www.gnu.org/licenses/>.

import socket
import os
from colorama import Fore
from medusa.config.utils import linux_socket_status

linux_status: dict = linux_socket_status()

def scan(host: str, ports: int) -> str:

    for port in ports:
        client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        code: int = client.connect_ex((host, port))

        if code == 0:
            print('[+] port ' + Fore.BLUE + port + Fore.WHITE + 'open for ' + Fore.CYAN + host)

        else:
            for value, status in linux_socket_status.items():
                if value == code:
                    print('[!] client returned code ' + Fore.RED + value + Fore.WHITE + '-' + Fore.RED + status + Fore.White + 'for port ' + Fore.YELLOW + port + Fore.WHITE + 'on ' + Fore.BLUE + host)
