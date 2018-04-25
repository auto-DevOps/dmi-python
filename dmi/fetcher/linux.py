#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   linux.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import os
import struct

from ..parser import (
    DMIParser,
    SMBIOSEntryPointParser,
)


class DMIFetcher(object):

    DMI_PATH = '/sys/firmware/dmi/tables/DMI'

    MEM_PATH = '/dev/mem'
    MEM_AREA_OFFSET = 0xf0000
    MEM_AREA_SIZE = 0x10000

    def load_mem_area(self, offset, size):
        fmem = open(self.MEM_PATH, 'rb')

        fmem.seek(offset)
        area = fmem.read(size)

        return area

    def load_sm(self, area, offset):
        entry_point = SMBIOSEntryPointParser().parse(
            content=area,
            offset=offset,
        )
        if not entry_point:
            return

        dmi_content = self.load_mem_area(
            offset=entry_point['structure_table_address'],
            size=entry_point['structure_table_length'],
        )

        return dmi_content

    def load_dmi_from_mem_file(self):
        area = self.load_mem_area(
            offset=self.MEM_AREA_OFFSET,
            size=self.MEM_AREA_SIZE,
        )

        start = 0
        while True:
            idx = area.find('_SM_', start)
            if idx == -1:
                break

            if idx % 16 == 0:
                return self.load_sm(area=area, offset=idx)

            start = idx + 1

    def fetch(self):
        if os.path.exists(self.DMI_PATH):
            content = open(self.DMI_PATH, 'rb').read()
            return DMIParser().parse(content=content)

        if os.path.exists(self.MEM_PATH):
            content = self.load_dmi_from_mem_file()
            if not content:
                return

            return DMIParser().parse(content=content)
