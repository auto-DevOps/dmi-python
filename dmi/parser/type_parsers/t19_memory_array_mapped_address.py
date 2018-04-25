#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t19_memory_array_mapped_address.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

from ..type import (
    DMIType,
)

from .base import (
    BaseParser,
)


@DMIType.register_parser
class TypeMemoryArrayMappedAddressParser(BaseParser):

    TYPE = DMIType.TYPE_MEMORY_ARRAY_MAPPED_ADDRESS
    TITLE = 'Memory Array Mapped Address'

    TYPE_FMTS = BaseParser.create_type_formats([
        ('2.1', '2BH2IHB'),
        ('2.7', '2I'),
    ])

    fields = (
        'type',
        'length',
        'handle',

        'starting_address',
        'ending_address',
        'memory_array_handle',
        'partition_width',

        'extended_starting_address',
        'extended_ending_address',
    )

    string_fields = (
    )
