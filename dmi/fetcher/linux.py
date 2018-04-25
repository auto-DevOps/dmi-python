#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   linux.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import os

from ..parser import (
    DMIParser,
)


class DMIFetcher(object):

    DMI_PATH = '/sys/firmware/dmi/tables/DMI'

    def __init__(self):
        self

    def fetch(self):
        if os.path.exists(self.DMI_PATH):
            content = open(self.DMI_PATH, 'rb').read()
            return DMIParser().parse(content=content)
