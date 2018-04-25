#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t17_memory_device.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import struct

from ..type import (
    DMIType,
)

from .base import (
    BaseParser,
)


@DMIType.register_parser
class TypeMemoryDeviceParser(BaseParser):

    TYPE = DMIType.TYPE_MEMORY_DEVICE
    TITLE = 'Memory Device'

    TYPE_FMTS = BaseParser.create_type_formats([
        ('2.1', '2B6H5BH'),
        ('2.3', 'H4B'),
        ('2.6', 'B'),
        ('2.7', 'IH'),
        ('2.8', '3H'),
    ])

    fields = (
        'type',
        'length',
        'handle',
        'physical_memory_array_handle',
        'memory_error_information_handle',
        'total_width',
        'data_width',
        'size',
        'form_factor',
        'device_set',
        'device_locator',
        'bank_locator',
        'memory_type',
        'type_detail',
        'speed',
        'manufacturer',
        'serial_number',
        'asset_tag',
        'part_number',
        'attributes',
        'extended_size',
        'configured_memory_clock_speed',
        'minimum_voltage',
        'maximum_voltage',
        'configured_voltage',
    )

    string_fields = (
        'device_locator',
        'bank_locator',
        'manufacturer',
        'serial_number',
        'asset_tag',
        'part_number',
    )
