#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : operation.py
 @Time       : 2021/2/15 11:25
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2021, iFuture Corporation Limited.
"""
import re
from utils.color import Colored
from configs.constant import (XPATH_EXTRACTOR, JSON_EXTRACTOR, CSS_EXTRACTOR,
                              REDIS_EXTRACTOR, FUNCTION_EXTRACTOR, REPLACE_EXTRACTOR,
                              REGEX_EXTRACTOR, FORMAT_EXTRACTOR, EXECUTE_EXTRACTOR,
                              GREATER_THAN ,LIST)
from exceptions import (XpathException, JsonException, CSSException, FormatException)
from utils.decorator import return_one_self
from lxml.etree import _Element
from bs4.element import Tag
from typing import List, Optional

MATCH_TOKEN = re.compile(r'{([a-zA-Z_].*)}')


class Operation(object):
    def __init__(self, name: str, script: str, target,
                 one_or_list: str = LIST):
        """
        初始化
        :param name: 名称，如是xpath, json, css, function, redis, execute, format, regex, replace
        :param script: 执行的语句操作，如xpath就是xpath语句等
        :param target: 目标，如function的话就是入参
        :param one_or_list: 返回list还是单个
        """
        self.name = name
        self.script = script
        self.target = target
        self.one_or_list = one_or_list if one_or_list else LIST

    def __str__(self):
        return Colored.yellow(f"[{self.name}] <Operation [{self.script}]"
                              f" [{self.target}]>")

    def execute(self):
        result: Optional[List[str], str] = None
        if self.name == XPATH_EXTRACTOR:
            result = self._xpath_execute()
        elif self.name == JSON_EXTRACTOR:
            result = self._json_execute()
        elif self.name == CSS_EXTRACTOR:
            result = self._xpath_execute()
        elif self.name == REDIS_EXTRACTOR:
            pass
        elif self.name == FUNCTION_EXTRACTOR:
            pass
        elif self.name == REPLACE_EXTRACTOR:
            pass
        elif self.name == REGEX_EXTRACTOR:
            pass
        elif self.name == FORMAT_EXTRACTOR:
            result = self._format_execute()
        elif self.name == EXECUTE_EXTRACTOR:
            result = self._execute_execute()
        return result

    @return_one_self
    def _xpath_execute(self):
        if isinstance(self.target, _Element):
            match_data = self.target.xpath(self.script)
            return match_data
        else:
            raise XpathException("core.model.Operation._xpath_execute", self.script)

    @return_one_self
    def _css_execute(self):
        if isinstance(self.target, Tag):
            return self.target.select(self.script)
        else:
            raise CSSException("core.model.Operation._css_execute", self.script)

    @return_one_self
    def _json_execute(self):
        # 形如 a > b > c
        if isinstance(self.target, dict):
            all_words = self.script.split()
            current_node = self.target
            for w in all_words:
                if w == GREATER_THAN:
                    pass
                else:
                    if isinstance(current_node, dict):
                        current_node = current_node.get(w)
                    elif isinstance(current_node, list):
                        current_node = [c.get(w) for c in current_node]
            return current_node
        else:
            raise JsonException("core.model.Operation._json_execute", self.script)

    @return_one_self
    def _format_execute(self):
        parameters = MATCH_TOKEN.findall(self.script)
        result = {}
        for p in parameters:
            try:
                v = self.target.get(p)
                result.setdefault(p, v)
            except Exception:
                raise FormatException("core.model.Operation._format_execute", self.script, p)
        return self.script.format(**result)

    @return_one_self
    def _execute_execute(self):
        raise NotImplementedError

