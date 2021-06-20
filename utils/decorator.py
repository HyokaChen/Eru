#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : decorator.py
 @Time       : 2021/4/11 14:04
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2021, iFuture Corporation Limited.
"""
import functools
from configs.constant import ONE
from typing import List, Generator


def return_one_self(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            if self.one_or_list == ONE:
                if isinstance(result, List):
                    return result[0]
                elif isinstance(result, Generator):
                    return next(result)
            return result
        except Exception as e:
            raise e
    return wrapper
