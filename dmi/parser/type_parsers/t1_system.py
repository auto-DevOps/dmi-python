#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t1_system.py
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
class TypeSystemParser(BaseParser):

    TYPE = DMIType.TYPE_SYSTEM
    TITLE = 'System Information'

    TYPE_FMTS = BaseParser.create_type_formats([
        ('2.0', '2BH4B'),
        ('2.1', '16sB'),
        ('2.4', '2B'),
    ])

    fields = (
        'type',
        'length',
        'handle',

        'manufacturer',
        'product_name',
        'version',
        'serial_number',

        'uuid',
        'wakeup_type',

        'sku_number',
        'family',
    )

    string_fields = (
        'manufacturer',
        'product_name',
        'version',
        'serial_number',
        'sku_number',
    )
