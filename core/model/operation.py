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
import ast
from utils.color import Colored
from configs.constant import (XPATH_EXTRACTOR, JSON_EXTRACTOR, CSS_EXTRACTOR,
                              REDIS_EXTRACTOR, FUNCTION_EXTRACTOR, REPLACE_EXTRACTOR,
                              REGEX_EXTRACTOR, FORMAT_EXTRACTOR, EXECUTE_EXTRACTOR,
                              GREATER_THAN, LIST)
from exceptions import (XpathException, JsonException, CSSException, FormatException)
from utils.decorator import return_one_self
from lxml.etree import _Element
from bs4.element import Tag
from typing import List, Optional

MATCH_TOKEN = re.compile(r'{([a-zA-Z_].*)}')


class Operation(object):
    def __init__(self, name: str, script: str, target, extra: dict,
                 one_or_list: str = LIST):
        """
        初始化
        :param name: 名称，如是xpath, json, css, function, redis, execute, format, regex, replace
        :param script: 执行的语句操作，如xpath就是xpath语句等
        :param target: 目标，如function的话就是入参
        :param extra: 额外数据
        :param one_or_list: 返回list还是单个
        """
        self.name = name
        self.script = script
        self.target = target
        self.extra = extra
        self.one_or_list = one_or_list if one_or_list else LIST

    def __str__(self):
        return Colored.yellow(f"[{self.name}] <Operation [{self.script}]"
                              f" [{self.target}]>")

    def execute(self):
        """
        执行
        :return:
        """
        result: Optional[List[str], str] = None
        if self.name == XPATH_EXTRACTOR:
            result = self._xpath_execute()
        elif self.name == JSON_EXTRACTOR:
            result = self._json_execute()
        elif self.name == CSS_EXTRACTOR:
            result = self._xpath_execute()
        elif self.name == REDIS_EXTRACTOR:
            result = self._redis_execute()
        elif self.name == FUNCTION_EXTRACTOR:
            result = self._function_execute()
        elif self.name == REPLACE_EXTRACTOR:
            result = self._replace_execute()
        elif self.name == REGEX_EXTRACTOR:
            result = self._regex_execute()
        elif self.name == FORMAT_EXTRACTOR:
            result = self._format_execute()
        elif self.name == EXECUTE_EXTRACTOR:
            result = self._execute_execute()
        return result

    @return_one_self
    def _xpath_execute(self):
        """
        xpath 解析
        :return:
        """
        if isinstance(self.target, _Element):
            match_data = self.target.xpath(self.script)
            return match_data
        else:
            raise XpathException("core.model.Operation._xpath_execute", self.script)

    @return_one_self
    def _css_execute(self):
        """
        css 选择器解析
        example: css#id
                 attribute: href
        :return:
        """
        if isinstance(self.target, Tag):
            res = self.target.select(self.script)
            flag = True if self.extra and 'attribute' in self.extra else False
            if flag:
                return res.attrs[self.extra['attribute']].strip()
            else:
                return res.get_text('\n\n', strip=True).strip()
        else:
            raise CSSException("core.model.Operation._css_execute", self.script)

    @return_one_self
    def _json_execute(self):
        """
        json 解析,
        example: a > b > c
        :return:
        """
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
        """
        格式化占位符解析
        example: {name}
        :return:
        """
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
        """
        执行语句解析
        example: {name} + 1
        :return:
        """
        # TODO: ast.literal_eval
        raise NotImplementedError

    @return_one_self
    def _regex_execute(self):
        """
        正则表达式解析
        :return:
        """
        raise NotImplementedError

    @return_one_self
    def _replace_execute(self):
        """
        替换内容解析
        :return:
        """
        # TODO：可能可以用flashtext
        raise NotImplementedError

    @return_one_self
    def _function_execute(self):
        """
        函数执行解析
        :return:
        """
        raise NotImplementedError

    @return_one_self
    def _redis_execute(self):
        """
        调用redis 数据解析
        :return:
        """
        raise NotImplementedError
