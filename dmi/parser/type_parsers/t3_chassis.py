#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t3_chassis.py
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
class TypeChassisParser(BaseParser):

    TYPE = DMIType.TYPE_CHASSIS
    TITLE = 'System Enclosure or Chassis'

    TYPE_FMTS = BaseParser.create_type_formats([
        ('2.0', '2BH5B'),
        ('2.1', '4B'),
        ('2.3', 'I4B'),
    ])

    fields = (
        'type',
        'length',
        'handle',
        'manufacturer',
        'type',
        'version',
        'serial_number',
        'asset_tag_number',
        'bootup_state',
        'power_supply_state',
        'thermal_state',
        'security_status',
        'oem_defined',
        'height',
        'number',
        'contained_element_count',
        'contained_element_record_length',
        'contained_elements',
        'sku_number',
    )

    string_fields = (
        'manufacturer',
        'version',
        'serial_number',
        'asset_tag_number',
    )
