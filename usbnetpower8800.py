#!/usr/bin/env python

# Copyright (C) 2011  Paul Marks  http://www.pmarks.net/
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# This is a simple command-line tool for controlling the USB Net Power 8800.
# It's basically a box with a USB port and a switchable power outlet.  It
# shows up under "lsusb" as:
#     ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port
#
# But, from what I can tell, none of the serial port features are ever used,
# and all you really need is one USB control transfer for reading the current
# state, and another for setting it.
#
# This hardware has the unfortunate property that unplugging its USB port
# immediately kills the power, which reduces its usefulness.

import sys
import usb.core

usage = (
    "Controller for the USB Net Power 8800\n"
    "Usage: %s on|off|toggle\n")

def IsPowerOn():
    # Return True if the power is currently switched on.
    ret = dev.ctrl_transfer(0xc0, 0x01, 0x0081, 0x0000, 0x0001)
    return ret[0] == 0xa0

def SetPower(on):
    # If True, turn the power on, else turn it off.
    code = 0xa0 if on else 0x20
    dev.ctrl_transfer(0x40, 0x01, 0x0001, code, [])

# Find the device.
dev = usb.core.find(idVendor=0x067b, idProduct=0x2303)
if dev is None:
    raise ValueError("Device not found")

try:
    cmd = sys.argv[1].lower()
except IndexError:
    cmd = ""

if cmd == "on":
    SetPower(True)
elif cmd == "off":
    SetPower(False)
elif cmd == "toggle":
    SetPower(not IsPowerOn())
else:
    sys.stdout.write(usage % sys.argv[0])
