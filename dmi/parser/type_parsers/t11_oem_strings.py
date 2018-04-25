#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t11_oem_strings.py
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
class TypeOEMStringsParser(BaseParser):

    TYPE = DMIType.TYPE_OEM_STRINGS
    TITLE = 'OEM Strings'

    def parse(self, content, strs=()):
        info = super(TypeOEMStringsParser, self).parse(
            content=content,
            strs=strs,
        )

        info['strings'] = strs

        return info
