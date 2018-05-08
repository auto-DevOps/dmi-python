#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   windows.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import ctypes

from ..parser import (
    DMIParser,
)


class DMIFetcher(object):

    kernel32 = ctypes.windll.kernel32

    #1381190978
    SIGNATURE_RSMB = 0
    for x in b'RSMB':
        SIGNATURE_RSMB = SIGNATURE_RSMB << 8 | x

    def fetch(self):
        kernel32 = self.kernel32
        if not kernel32:
            return

        get_firmware = kernel32.GetSystemFirmwareTable

        # query size in order to prepare buffer
        bios_size = get_firmware(
            self.SIGNATURE_RSMB,
            0,
            0,
            0,
        )
        if not bios_size:
            return

        # create buffer
        buf = ctypes.create_string_buffer(bios_size)

        # query table
        bios_size = get_firmware(
            self.SIGNATURE_RSMB,
            0,
            buf,
            bios_size,
        )
        if not bios_size:
            return

        # remove 8 byte header
        content = buf.raw[8:]

        return DMIParser().parse(content=content)
