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
from asyncio.events import AbstractEventLoop
from configs.constant import TEMPLATE_PATH
from core.model.template import BaseTemplate
from typing import Optional


class Eru(object):
    """
    千反田爱瑠
    """
    __slots__ = [
        'loop',
        'template',
    ]

    def __init__(self, loop: AbstractEventLoop,
                 path: Optional[str]) -> None:
        self.loop = loop
        # TODO: 通过 watch 模板，来动态更新pg数据库，同时更新redis中的任务
        # 文件（基础配置） -> Redis -> 数据库（备份，以及启动状态和定时）
        path = path if path else TEMPLATE_PATH
        self.template = self._read_template(path)

    def _read_template(self, path: str) -> BaseTemplate:
        pass

    async def start(self):
        pass

    async def stop(self):
        pass

