#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t32_system_boot.py
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
class TypeSystemBootParser(BaseParser):

    TYPE = DMIType.TYPE_SYSTEM_BOOT
    TITLE = 'System Boot Information'

    TYPE_FMTS = BaseParser.create_type_formats([
        ('', '2BH6s'),
    ])

    fields = (
        'type',
        'length',
        'handle',
        'reserved',
    )

    string_fields = (
    )
