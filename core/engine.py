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
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from asyncio.events import AbstractEventLoop
from core.model.template import BaseTemplate
import toml
from configs.constant import TEMPLATE_PATH
from typing import Optional


class Eru(FileSystemEventHandler):
    """
    千反田爱瑠
    """
    __slots__ = [
        'template',
    ]

    def __init__(self) -> None:
        # TODO: 通过 watch 模板，来动态更新pg数据库，同时更新redis中的任务
        # 文件（基础配置） -> Redis -> 数据库（备份，以及启动状态和定时）
        super().__init__()
        self._read_template(TEMPLATE_PATH + '/正义网.toml')

    def on_created(self, event: FileSystemEvent):
        if not event.is_directory:
            self._read_template(event.src_path)

    def on_deleted(self, event: FileSystemEvent):
        if not event.is_directory:
            self._read_template(event.src_path)

    def on_modified(self, event: FileSystemEvent):
        if not event.is_directory:
            self._read_template(event.src_path)

    def _read_template(self, path: str) -> None:
        with open(path, mode='r', encoding='utf-8') as f:
            file_data = toml.loads(f.read())
            base_template = BaseTemplate(**file_data)
            print(base_template)
            # file_data字典 > BaseTemplate


class Hyoka(object):
    """
    冰菓
    """
    __slots__ = [
        'loop',
    ]

    def __init__(self, loop: AbstractEventLoop):
        self.loop = loop

    def start(self):
        pass

    def stop(self):
        pass

