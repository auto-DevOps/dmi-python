#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t127_end_of_table.py
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

    TYPE = DMIType.TYPE_END_OF_TABLE
    TITLE = 'End of Table'

    TYPE_FMTS = BaseParser.create_type_formats([
        ('', '2BH'),
    ])

    fields = (
        'type',
        'length',
        'handle',
    )

    string_fields = (
    )
