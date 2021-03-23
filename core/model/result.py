#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : result.py
 @Time       : 2021/2/12 12:39
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2021, iFuture Corporation Limited.
"""
from dataclasses import dataclass, field
from core.model.operation import Operation
from utils.color import Colored
from typing import Dict


@dataclass
class ResultTemplate(object):
    result_id: int
    field_dict: Dict[str, Operation] = field(default_factory=dict)
    global_parameter: str = None

    def __str__(self):
        return Colored.yellow(f"[{self.result_id}] <Result>")

    def __contains__(self, item):
        return True if item.result_id == self.result_id else False
