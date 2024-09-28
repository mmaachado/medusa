#!/bin/usr/python
#
# Filename: medusa.py
# Description: Medusa is a multipurpose hacking tool.
# Author: marques <uniqueduckinbox at duck.com>
# URL: https://github.com/mmaachado/medusa
# Keywords: Medusa Offensive Security PenTest Red Team
# Compatibility: python-version >= 3.12.5
#
# ----------------------------
#
# Commentary:
#
# this is the start of Medusa
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


from colorama import Fore
import argparse
import subprocess

banner: str = r"""
 __    __    ______    _____     __  __    ______    ______    
/\ "-./  \  /\  ___\  /\  __-.  /\ \/\ \  /\  ___\  /\  __ \   
\ \ \-./\ \ \ \  __\  \ \ \/\ \ \ \ \_\ \ \ \___  \ \ \  __ \  
 \ \_\ \ \_\ \ \_____\ \ \____-  \ \_____\ \/\_____\ \ \_\ \_\ 
  \/_/  \/_/  \/_____/  \/____/   \/_____/  \/_____/  \/_/\/_/ 
                                                                   
v 0.1

"""

print(Fore.GREEN + banner)

def commands(cmd: str):
    try:
        subprocess.check_call(cmd, shell=True)
    except:
        pass

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

sync_group = parser.add_argument_group('sync repository')
port_scanning_group = parser.add_argument_group('port scanning')
passive_scanning_group = parser.add_argument_group('passive scanning')

port_scanning_group.add_argument('-p', '--port_scan', type=str,help='scan for open ports', metavar='80,21,22,23,25,443,445,8080,3306,139,135')
passive_scanning_group.add_argument('-s', type=str, help='scan for subdomains', metavar='<domain.com>')

parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity.')
parser.add_argument('-c', '--concurrency', type=int, default=10, help='maximum number of concurrent requests.')

sync_group.add_argument('-S', '--sync', action='store_true', help='synchronize the repository with the master branch.')
sync_group.add_argument('-y', '--refresh', action='store_true', help='refresh all dependencies according to `pyproject.toml` or `requirements.txt`')
sync_group.add_argument('-u', '--upgrade', action='store_true', help='upgrade all dependencies to the latest release and locks to `pyproject.toml` or freeze to `requirements.txt`')

args = parser.parse_args()

if args.sync:
    print(Fore.YELLOW + '[!] synchronising package. . .')
    commands('git pull')
    print(Fore.GREEN + '[*] package synchronized with master!\n')

if args.refresh:
    print(Fore.YELLOW + '[!] refreshing dependencies. . .')
    try:
        commands('poetry install --sync')
    except:
        commands('pip install -r requirements.txt')

if args.upgrade:
    print(Fore.YELLOW + '\n[!] upgrading dependencies. . .')
    try:
        commands('poetry update')
    except:
        commands('pip-review --auto')
        commands('pip freeze > requirements.txt')
