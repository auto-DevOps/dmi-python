#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   __init__.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import json

from .parser import (
    DMIParser,
)
from .fetcher import (
    DMIFetcher,
)


def fetch_dmi():
    return DMIFetcher().fetch()


def print_dmi_jsonic():
    print(json.dumps(
        fetch_dmi(),
        ensure_ascii=False,
        indent=4,
        default=lambda obj: str(obj),
    ))
