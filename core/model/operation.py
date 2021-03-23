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
from utils.color import Colored
from configs.constant import (XPATH_EXTRACTOR, JSON_EXTRACTOR, CSS_EXTRACTOR,
                              REDIS_EXTRACTOR, FUNCTION_EXTRACTOR, REPLACE_EXTRACTOR,
                              REGEX_EXTRACTOR, FORMAT_EXTRACTOR, EXECUTE_EXTRACTOR,
                              ONE, LIST, MARK, WAVE)
from lxml.etree import _Element
from bs4.element import Tag
from typing import List, Optional


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
        self.one_or_list = one_or_list

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
            pass
        elif self.name == EXECUTE_EXTRACTOR:
            pass
        return result

    def _xpath_execute(self):
        if isinstance(self.target, _Element):
            match_data = self.target.xpath(self.script)
            if self.one_or_list == ONE:
                return match_data[0]
            elif self.one_or_list == LIST:
                return match_data
        else:
            raise Exception(f"[core.model.Operation._xpath_execute()]{self.script} XPath 语法不能执行，"
                            f"因为target不是 XPath 实例")

    def _css_execute(self):
        if isinstance(self.target, Tag):
            if self.one_or_list == ONE:
                return self.target.select_one(self.script)
            elif self.one_or_list == LIST:
                return self.target.select(self.script)
        else:
            raise Exception(f"[core.model.Operation._css_execute()]{self.script} CSS Selector语法不能执行，"
                            f"因为target不是 BeautifulSoup4 实例")

    def _json_execute(self):
        # 形如 a ! b ~ c  代表 a 是单个字典，内部的b是列表，再从中提取 c
        if isinstance(self.target, dict):
            all_words = self.script.split()
            current_node = self.target
            for w in all_words:
                if w not in (MARK, WAVE):
                    if isinstance(current_node, dict):
                        current_node = current_node.get(w)
                    elif isinstance(current_node, list):
                        current_node = [c.get(w) for c in current_node]
                elif w == MARK:
                    pass
        else:
            raise Exception(f"[core.model.Operation._json_execute()]{self.script} Json 抽取语法不能执行，"
                            f"因为target不是 dict 实例")
