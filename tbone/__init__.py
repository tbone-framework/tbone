#!/usr/bin/env python
# encoding: utf-8

VERSION = (0, 0, 1)

__short_version__ = '.'.join(map(str, VERSION[0:2]))
__version__ = ''.join(['.'.join(map(str, VERSION[0:3])), ''.join(VERSION[3:])])