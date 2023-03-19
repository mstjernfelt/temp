#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2017 Zomboided
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#    Module for apending DNS.

from libs.utility import debugTrace, errorTrace

def appendDNS():
    """
    This function appends the nameservers to /etc/resolv.conf.
    """
    debugTrace('Appending DNS to /etc/resolv.conf')
    to_write = "nameserver 103.86.96.100\nnameserver 103.86.99.100"

    try:
        with open('/etc/resolv.conf', 'w') as file:
            file.write(to_write)

    except PermissionError:
        errorTrace('dns.py', 'Unable to write to /etc/resolv.conf, permission denied.')
