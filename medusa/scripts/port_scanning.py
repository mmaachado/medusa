#!/bin/usr/python
#
# Filename: port_scanning.py
# Description: Powerfull tool to check every open port
# Author: marques <uniqueduckinbox at duck.com>
# URL: https://github.com/mmaachado/medusa
# Keywords: Medusa Offensive Security PenTest Red Team Port Scan
# Compatibility: python-version >= 3.10.1
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
from colorama import Fore

# TODO - remove this giant dict from here, put in a csv file to read or something better.

status_code: dict = {
        1 : 'Operation not permitted', 2 : 'No such file or directory',
        3 : 'No such process', 4 : 'Interrupted system call',
        5 : 'Input/output error', 6 : 'No such device or address',
        7 : 'Argument list too long', 8 : 'Exec format error',
        9 : 'Bad file descriptor', 10 : 'No child processes',
        11 : 'Resource temporarily unavailable', 12 : 'Cannot allocate memory',
        13 : 'Permission denied', 14 : 'Bad address', 15 : 'Block device required',
        16 : 'Device or resource busy',
        17 : 'File exists', 18 : 'Invalid cross-device link', 19 : 'No such device',
        20 : 'Not a directory', 21 : 'Is a directory', 22 : 'Invalid argument',
        23 : 'Too many open files in system', 24 : 'Too many open files',
        25 : 'Inappropriate ioctl for device', 26 : 'Text file busy',
        27 : 'File too large', 28 : 'No space left on device',
        29 : 'Illegal seek', 30 : 'Read-only file system', 31 : 'Too many links', 
        32 : 'Broken pipe', 33 : 'Numerical argument out of domain',
        34 : 'Numerical result out of range',
        35 : 'Resource deadlock avoided', 36 : 'File name too long',
        37 : 'No locks available', 38 : 'Function not implemented',
        39 : 'Directory not empty', 40 : 'Too many levels of symbolic links',
        41 : 'Unknown error 41', 42 : 'No message of desired type',
        43 : 'Identifier removed', 44 : 'Channel number out of range',
        45 : 'Level 2 not synchronized', 46 : 'Level 3 halted', 47 : 'Level 3 reset',
        48 : 'Link number out of range', 49 : 'Protocol driver not attached',
        50 : 'No CSI structure available', 51 : 'Level 2 halted', 52 : 'Invalid exchange',
        53 : 'Invalid request descriptor', 54 : 'Exchange full',
        55 : 'No anode', 56 : 'Invalid request code', 57 : 'Invalid slot',
        58 : 'Unknown error 58', 59 : 'Bad font file format',
        60 : 'Device not a stream', 61 : 'No data available',
        62 : 'Timer expired', 63 : 'Out of streams resources',
        64 : 'Machine is not on the network', 65 : 'Package not installed',
        66 : 'Object is remote', 67 : 'Link has been severed', 69 : 'Srmount error',
        70 : 'Communication error on send', 71 : 'Protocol error',
        72 : 'Multihop attempted', 73 : 'RFS specific error', 75 : 'Value too large for defined data type',
        76 : 'Name not unique on network', 77 : 'File descriptor in bad state',
        78 : 'Remote address changed',
        79 : 'Can not access a needed shared library', 80 : 'Accessing a corrupted shared library',
        81 : '.lib section in a.out corrupted',
        82 : 'Attempting to link in too many shared libraries', 83 : 'Cannot exec a shared library directly',
        84 : 'Invalid or incomplete multibyte or wide character', 85 : 'Interrupted system call should be restarted',
        86 : 'Streams pipe error', 87 : 'Too many users',
        88 : 'Socket operation on non-socket', 89 : 'Destination address required',
        90 : 'Message too long', 91 : 'Protocol wrong type for socket',
        92 : 'Protocol not available', 93 : 'Protocol not supported',
        94 : 'Socket type not supported', 95 : 'Operation not supported',
        96 : 'Protocol family not supported', 97 : 'Address family not supported by protocol',
        98 : 'Address already in use', 99 : 'Cannot assign requested address', 
        100 : 'Network is down', 101 : 'Network is unreachable',
        102 : 'Network dropped connection on reset', 103 : 'Software caused connection abort', 
        104 : 'Connection reset by peer', 105 : 'No buffer space available',
        106 : 'Transport endpoint is already connected', 107 : 'Transport endpoint is not connected',
        108 : 'Cannot send after transport endpoint shutdown', 109 : 'Too many references: cannot splice',
        110 : 'Connection timed out', 111 : 'Connection refused',
        112 : 'Host is down', 113 : 'No route to host',
        114 : 'Operation already in progress', 115 : 'Operation now in progress',
        116 : 'Stale NFS file handle', 117 : 'Structure needs cleaning',
        118 : 'Not a XENIX named type file', 119 : 'No XENIX semaphores available',
        120 : 'Is a named type file', 121 : 'Remote I/O error',
        122 : 'Disk quota exceeded', 123 : 'No medium found',
        124 : 'Wrong medium type',
    }

def scan(host: str, ports: int) -> str:

    print(Fore.BLUE + 'PORT SCANNING TARGET\n')

    for port in ports:
        client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        code: int = client.connect_ex((host, port))

        if code == 0:
            print(Fore.GREEN + f'[+] port {port} open for {host}')

        else:
            for value, status in status_code.items():
                if value == code:
                    print(Fore.YELLOW + f'[!] {host}: {code} {status} on port {port}')
