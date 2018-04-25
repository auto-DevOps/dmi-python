#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   t126_inactive.py
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
class TypeInactiveParser(BaseParser):

    TYPE = DMIType.TYPE_INACTIVE
    TITLE = 'Inactive'
