#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   base.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import struct

from collections import (
    OrderedDict,
)


def create_type_formats(fragments):
    formats = OrderedDict()

    fmt = '='
    for version, fragment in fragments:
        fmt += fragment
        formats[version] = struct.Struct(fmt)

    return formats


class BaseParser(object):

    TITLE = 'Base'

    TYPE_FMTS = create_type_formats([
        ('', 'BBH'),
    ])

    fields = (
        'type',
        'length',
        'handle',
    )

    string_fields = (
    )

    create_type_formats = staticmethod(create_type_formats)

    def parse(self, content, strs=()):
        content_size = len(content)

        for fmt in self.TYPE_FMTS.values():
            if fmt.size == content_size:
                break

        values = fmt.unpack(content[:fmt.size])

        data_inject = [
            ('title', self.TITLE),
        ]
        data = list(zip(self.fields, values))

        info = OrderedDict(data_inject + data)
        for field in self.string_fields:
            if field in info:
                info[field] = strs[info[field]-1]

        return info
