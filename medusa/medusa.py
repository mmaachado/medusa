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

banner: str = r"""
 __    __    ______    _____     __  __    ______    ______    
/\ "-./  \  /\  ___\  /\  __-.  /\ \/\ \  /\  ___\  /\  __ \   
\ \ \-./\ \ \ \  __\  \ \ \/\ \ \ \ \_\ \ \ \___  \ \ \  __ \  
 \ \_\ \ \_\ \ \_____\ \ \____-  \ \_____\ \/\_____\ \ \_\ \_\ 
  \/_/  \/_/  \/_____/  \/____/   \/_____/  \/_____/  \/_/\/_/ 
                                                                   
v 0.1

"""

print(Fore.GREEN + banner)
