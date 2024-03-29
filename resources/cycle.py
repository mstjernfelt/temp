#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2016 Zomboided
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
#    This module does the same as calling the cycle function from the add-on
#    menu screen but allows a user to configure it to a button on a remote, etc

from libs.common import requestVPNCycle
from libs.utility import debugTrace, errorTrace, infoTrace, newPrint, getID
from dns import appendDNS

# Call the common cycle routine
appendDNS()

debugTrace("-- Entered cycle.py --")
if not getID() == "":
    requestVPNCycle(False)
else:
    errorTrace("cycle.py", "VPN service is not ready")
debugTrace("-- Exit cycle.py --")
