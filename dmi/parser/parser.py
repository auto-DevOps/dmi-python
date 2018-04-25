#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   parser.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import struct

from .type import (
    DMIType,
)


class DMIParser(object):

    DMI_HEADER_FMT = struct.Struct('@2BH')
    DMI_HEADER_SIZE = DMI_HEADER_FMT.size

    get_parser = DMIType.get_parser

    def parse_string_area(self, content, start=0):
        '''
            Parse string area right after and DMI table item.
            String area is end of two '\0' bytes, strings are stored one by one.
        '''
        idx = content.find(b'\0\0', start)
        strs = content[start:idx].split(b'\0')
        return idx-start+2, strs

    def iter_dmi_table(self, content):
        '''
        '''
        cursor = 0
        content_size = len(content)

        while cursor < content_size:
            header = content[cursor:cursor+self.DMI_HEADER_SIZE]

            # parse header
            _type, length, _ = self.DMI_HEADER_FMT.unpack(header)

            # load the whole item by length found
            item_content = content[cursor:cursor+length]
            cursor += length

            # parse string area if any
            area_size, strs = self.parse_string_area(content, cursor)
            cursor += area_size

            # get parser for the specific type
            parser = self.get_parser(_type)
            if not parser:
                continue

            # call type parse to do further parsing
            item = parser().parse(content=item_content, strs=strs)
            yield item

    def parse(self, content):
        '''
        '''
        return [
            dmi
            for dmi in self.iter_dmi_table(content=content)
        ]
