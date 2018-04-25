#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   type.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

from .type_parsers.base import (
    BaseParser,
)


class DMIType(object):
    '''
          0   BIOS
          1   System
          2   Baseboard
          3   Chassis
          4   Processor
          5   Memory Controller
          6   Memory Module
          7   Cache
          8   Port Connector
          9   System Slots
         10   On Board Devices
         11   OEM Strings
         12   System Configuration Options
         13   BIOS Language
         14   Group Associations
         15   System Event Log
         16   Physical Memory Array
         17   Memory Device
         18   32-bit Memory Error
         19   Memory Array Mapped Address
         20   Memory Device Mapped Address
         21   Built-in Pointing Device
         22   Portable Battery
         23   System Reset
         24   Hardware Security
         25   System Power Controls
         26   Voltage Probe
         27   Cooling Device
         28   Temperature Probe
         29   Electrical Current Probe
         30   Out-of-band Remote Access
         31   Boot Integrity Services
         32   System Boot
         33   64-bit Memory Error
         34   Management Device
         35   Management Device Component
         36   Management Device Threshold Data
         37   Memory Channel
         38   IPMI Device
         39   Power Supply
         40   Additional Information
         41   Onboard Devices Extended Information
         42   Management Controller Host Interface
    '''

    TYPE_BIOS = 0
    TYPE_SYSTEM = 1
    TYPE_BASEBOARD = 2
    TYPE_CHASSIS = 3
    TYPE_PROCESSOR = 4

    TYPE_OEM_STRINGS = 11
    TYPE_PHYSICAL_MEMORY_ARRAY = 16
    TYPE_MEMORY_DEVICE = 17

    TYPE_MEMORY_ARRAY_MAPPED_ADDRESS = 19
    TYPE_SYSTEM_BOOT = 32

    TYPE_INACTIVE = 126
    TYPE_END_OF_TABLE = 127

    parsers = {
    }

    @classmethod
    def get_parser(cls, dmi_type):
        return cls.parsers.get(dmi_type, BaseParser)

    @classmethod
    def register_parser(cls, parser):
        cls.parsers[parser.TYPE] = parser
        return parser

from .type_parsers import (
    all as _,
)
