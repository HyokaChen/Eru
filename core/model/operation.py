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
import importlib
from flashtext import KeywordProcessor
from utils.color import Colored
from configs.constant import (XPATH_EXTRACTOR, JSON_EXTRACTOR, CSS_EXTRACTOR,
                              REDIS_EXTRACTOR, FUNCTION_EXTRACTOR, REPLACE_EXTRACTOR,
                              REGEX_EXTRACTOR, FORMAT_EXTRACTOR, EXECUTE_EXTRACTOR,
                              GREATER_THAN, LIST, TRANSFORM_TO, RESPONSE_EXTRACTOR)
from core.model.exceptions import *
from utils.decorator import return_one_self
from utils.db import redis_db
from lxml.etree import _Element
from httpx import Response
from bs4.element import Tag
from typing import List, Dict, Optional, Any, Union

MATCH_TOKEN = re.compile(r'{([a-zA-Z_].*)}')
MATCH_NUMBER = re.compile(r'\[(\d+)]', re.MULTILINE)


class Operation(object):
    def __init__(self, name: str, script: str,
                 target: Union[_Element, Tag, Dict, str, Response],
                 extra: Dict[str, Any],
                 one_or_list: str = LIST) -> None:
        """
        初始化
        :param name: 名称，如是xpath, json, css, function, redis, execute, format, regex, replace, response
        :param script: 执行的语句操作，如xpath就是xpath语句等
        :param target: 目标，如function的话就是入参
        :param extra: 额外数据
        :param one_or_list: 返回list还是单个
        """
        self.name: str = name
        self.script: str = script
        # 默认不写 target 目标则为网页的 lxml 或者 bs，或者 json
        self.target: Union[_Element, Tag, Dict, str, Response] = target
        self.extra: Dict[str, Any] = extra
        self.one_or_list: str = one_or_list if one_or_list else LIST

    def __str__(self):
        return Colored.yellow(f"[{self.name}] <Operation [{self.script}]"
                              f" [{self.target}]>")

    def execute(self) -> Union[str, List[str]]:
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
        elif self.name == RESPONSE_EXTRACTOR:
            result = self._response_execute()
        return result

    @return_one_self
    def _xpath_execute(self) -> Union[str, List[str]]:
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
    def _css_execute(self) -> Union[str, List[str], int]:
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
    def _json_execute(self) -> Union[str, List[str]]:
        """
        json 解析,
        example: a > b > c
        :return:
        """
        if isinstance(self.target, Dict):
            all_words = self.script.split(GREATER_THAN)
            # 添加 end 标记
            all_words.append('end')
            current_node = self.target
            for w in all_words:
                if isinstance(current_node, Dict):
                    current_node = current_node.get(w)
                elif isinstance(current_node, List):
                    if current_node:
                        if isinstance(current_node[0], Dict):
                            current_node = [c.get(w) for c in current_node]
                        elif isinstance(current_node[0], str):
                            current_node = [c for c in current_node]
                        elif isinstance(current_node[0], List):
                            current_node = [c for c in current_node]
                elif isinstance(current_node, str) or isinstance(current_node, int):
                    break
                # 处理下标
                match_number = MATCH_NUMBER.findall(w)
                if match_number and isinstance(current_node, List):
                    current_node = current_node[match_number[0]]
            return current_node
        else:
            raise JsonException("core.model.Operation._json_execute", self.script)

    @return_one_self
    def _format_execute(self) -> str:
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
    def _execute_execute(self) -> Union[str, int]:
        """
        执行语句解析
        example: {name} + 1
        :return:
        """
        # TODO: ast.literal_eval
        parameters = MATCH_TOKEN.findall(self.script)
        result = {}
        for p in parameters:
            try:
                v = self.target.get(p)
                result.setdefault(p, v)
            except Exception:
                raise ExecuteException("core.model.Operation._execute_execute", self.script, p)
        return ast.literal_eval(self.script.format(**result))

    @return_one_self
    def _regex_execute(self) -> Union[str, List[str]]:
        """
        正则表达式解析
        :return:
        """
        if isinstance(self.target, str):
            result = re.findall(self.script, self.target)
            if result:
                return result
            else:
                raise RegexException("core.model.Operation._regex_execute", self.script)
        else:
            raise RegexException("core.model.Operation._regex_execute", self.script)

    @return_one_self
    def _replace_execute(self) -> Union[str, List[str]]:
        """
        替换内容解析
        :return:
        """
        # TODO：可能可以用flashtext
        replace_a, to_b = self.script.split(TRANSFORM_TO)
        # 1. 初始化关键字处理器
        keyword_processor = KeywordProcessor(case_sensitive=True)
        # 2. 添加关键词
        keyword_processor.add_keyword(replace_a, to_b)
        try:
            if isinstance(self.target, str):
                # 3. 替换关键词
                return keyword_processor.replace_keywords(self.target)
            elif isinstance(self.target, List):
                return [keyword_processor.replace_keywords(s) for s in self.target]
            else:
                raise Exception()
        except Exception:
            raise RegexException("core.model.Operation._replace_execute", self.script)

    @return_one_self
    def _function_execute(self) -> Dict[str, Any]:
        """
        函数执行解析
        :return:
        """
        try:
            package, method = self.script.rsplit('.', 1)
            module = importlib.import_module(package)
            m = getattr(module, method)
            # TODO: 是否需要根据形参来动态function，而不是只传一个值
            return m(self.target)
        except Exception:
            raise FunctionException("core.model.Operation._function_execute", self.script)

    @return_one_self
    def _redis_execute(self) -> str:
        """
        调用redis 数据解析
        :return:
        """
        try:
            # 仅支持get
            return redis_db.get(self.script)
        except Exception:
            raise RedistException("core.model.Operation._redis_execute", self.script)

    @return_one_self
    def _response_execute(self) -> str:
        """
        解析抽取header
        :return:
        :rtype:
        """
        try:
            return self.target.headers.get(self.script)
        except Exception:
            raise ResponseException("core.model.Operation._response_execute", self.script)
