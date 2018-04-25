#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t2_baseboard.py
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
class TypeBaseboardParser(BaseParser):

    TYPE = DMIType.TYPE_BASEBOARD
    TITLE = 'Baseboard Information'

    TYPE_FMTS = BaseParser.create_type_formats([
        ('', '2BH7BH2B'),
    ])

    fields = (
        'type',
        'length',
        'handle',
        'manufacturer',
        'product',
        'version',
        'serial_number',
        'asset_tag',
        'feature_flags',
        'location_in_chassis',
        'chassis_handle',
        'board_type',
        'number_of_contained_object_handles',
        'contained_object_handles',
    )

    string_fields = (
        'manufacturer',
        'product',
        'version',
        'serial_number',
        'asset_tag',
        'location_in_chassis',
    )
