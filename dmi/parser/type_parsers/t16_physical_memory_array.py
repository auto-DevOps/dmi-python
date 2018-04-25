#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t16_physical_memory_array.py
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
class TypeEndOfTableParser(BaseParser):

    TYPE = DMIType.TYPE_PHYSICAL_MEMORY_ARRAY
    TITLE = 'Physical Memory Array'

    TYPE_FMTS = BaseParser.create_type_formats([
        ('2.1', '2BH3BI2H'),
        ('2.7', 'Q')
    ])

    fields = (
        'type',
        'length',
        'handle',
        'location',
        'use',
        'memory_error_correction',
        'maximum_capacity',
        'memory_error_information_handle',
        'number_of_memory_devices',
        'extended_maximum_capacity',
    )

    string_fields = (
    )
