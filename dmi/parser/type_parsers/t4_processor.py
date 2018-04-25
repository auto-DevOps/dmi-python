#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t4_processor.py
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
class TypeProcessorParser(BaseParser):

    TITLE = 'Processor'
    TYPE = DMIType.TYPE_PROCESSOR

    TYPE_FMTS = BaseParser.create_type_formats([
        ('2.0', 'BBHBBBBQBBHHHBB'),
        ('2.1', 'HHH'),
        ('2.3', 'BBB'),
        ('2.5', 'BBBH'),
        ('2.6', 'H'),
        ('3.0', 'HHH'),
    ])

    fields = (
        'type',
        'length',
        'handle',
        'socket_designation',
        'processor_type',
        'processor_family',
        'processor_manufacturer',
        'processor_id',
        'processor_version',
        'voltage',
        'external_clock',
        'max_speed',
        'current_speed',
        'status',
        'processor_upgrade',
        'l1_cache_handle',
        'l2_cache_handle',
        'l3_cache_handle',
        'serial_number',
        'assert_tag',
        'part_number',
        'core_count',
        'core_enabled',
        'thread_count',
        'processor_characteristics',
        'processor_family2',
        'core_count2',
        'core_enabled2',
        'thread_count2',
    )

    string_fields = (
        'processor_manufacturer',
        'processor_version',
    )
