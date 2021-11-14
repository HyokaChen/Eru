#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : exceptions.py
 @Time       : 2021/4/11 13:39
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2021, iFuture Corporation Limited.
"""


class BaseError(Exception):
    def __init__(self, func, script, base_error):
        self.error_msg = f"[{func}()] {script} {base_error}"
        super().__init__(self, self.error_msg)


class XpathException(BaseError):
    def __init__(self, func, script):
        BaseError.__init__(self, func, script, "XPath 语法不能执行，因为target不是 XPath 实例")


class CSSException(BaseError):
    def __init__(self, func, script):
        BaseError.__init__(self, func, script, "CSS Selector语法不能执行，因为target不是 BeautifulSoup4 实例")


class JsonException(BaseError):
    def __init__(self, func, script):
        BaseError.__init__(self, func, script, "Json 抽取语法不能执行，因为target不是 dict 实例")


class FormatException(BaseError):
    def __init__(self, func, script, value):
        BaseError.__init__(self, func, script, f"Format 抽取语法不能执行，没有找到{value}")


class ExecuteException(BaseError):
    def __init__(self, func, script, value):
        BaseError.__init__(self, func, script, f"Execute 抽取语法不能执行，没有找到{value}")


class RegexException(BaseError):
    def __init__(self, func, script):
        BaseError.__init__(self, func, script, f"Regex 抽取语法不能执行")


class ReplaceException(BaseError):
    def __init__(self, func, script):
        BaseError.__init__(self, func, script, f"Replace 抽取语法不能执行")


class FunctionException(BaseError):
    def __init__(self, func, script):
        BaseError.__init__(self, func, script, f"Function 抽取语法不能执行")


class RedistException(BaseError):
    def __init__(self, func, script):
        BaseError.__init__(self, func, script, f"Redis 抽取语法不能执行")