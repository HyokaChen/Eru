#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : process.py
 @Time       : 2021/2/12 12:39
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2021, iFuture Corporation Limited.
"""
from dataclasses import dataclass
from configs.constant import JSON
from utils.color import Colored


@dataclass
class ProcessTemplate(object):
    process_id: int
    process_function: str = None
    parameters: str = None
    return_type: str = JSON

    def __str__(self):
        return Colored.yellow(f"[{self.process_id}] <Process [{self.process_function}]"
                              f" [{self.parameters}] [{self.return_type}] >")

    def __contains__(self, item):
        return True if item.process_id == self.process_id else False
