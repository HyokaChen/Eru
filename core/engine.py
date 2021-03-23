#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : engine.py
 @Time       : 2021/2/12 12:10
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2021, iFuture Corporation Limited.
"""
import os
from utils.color import Colored
from configs.constant import TEMPLATE_PATH
from core.model.template import BaseTemplate


class Eru(object):
    """
    千反田爱瑠
    """
    __slots__ = [
        'loop',
        'template',
    ]

    def __init__(self, loop):
        self.loop = loop
        self.template = self._read_template()

    def _read_template(self):


    async def start(self):
        pass

    async def stop(self):
        pass

