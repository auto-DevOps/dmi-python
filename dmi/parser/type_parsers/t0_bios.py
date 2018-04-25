#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t0_bios.py
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
class TypeBIOSParser(BaseParser):

    TYPE = DMIType.TYPE_BIOS
    TITLE = 'BIOS Information'

    TYPE_FMTS = BaseParser.create_type_formats([
        ('2.0', '2BH2BH2BQ'),
        ('2.4', '2sBBBB'),
        ('3.1', 'H'),
    ])

    fields = (
        'type',
        'length',
        'handle',
        'vendor',
        'bios_version',
        'bios_starting_address_segment',
        'bios_release_date',
        'bios_rom_size',
        'bios_characteristics',
        'bios_characteristics_extension_bytes',
        'system_bios_major_release',
        'system_bios_minor_release',
        'embedded_controller_firmware_major_release',
        'embedded_controller_firmware_minor_release',
    )

    string_fields = (
        'vendor',
        'bios_version',
        'bios_release_date',
    )

    def parse(self, content, strs=()):
        info = super(TypeBIOSParser, self).parse(content=content, strs=strs)

        if 'bios_rom_size' in info:
            info['bios_rom_size'] = (info['bios_rom_size'] + 1) * 64

        return info
