#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : template.py
 @Time       : 2021/2/12 12:39
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2021, iFuture Corporation Limited.
"""
from dataclasses import dataclass, field
from typing import List
from configs.constant import GET, HTML, NEWS
from core.model.request import RequestTemplate
from core.model.process import ProcessTemplate
from core.model.result import ResultTemplate


@dataclass
class BaseTemplate(object):
    START_URL: str
    SPIDER_NAME: str
    SITE_NAME: str
    METHOD: str = GET
    REFERER: str = None
    REQUESTS: List[RequestTemplate] = field(default_factory=list)
    PROCESSES: List[ProcessTemplate] = field(default_factory=list)
    RESULTS: List[ResultTemplate] = field(default_factory=list)
    NEED_RENDER: bool = False
    TIMEOUT: int = 200
    USE_PROXY: bool = False
    SLEEP_TIME: int = 10
    SESSION: bool = True
    COOKIES: str = None
    RETURN_TYPE: str = HTML
    DATA_TABLE: str = NEWS
    # 数字越小越靠快速消费
    PRIORITY: int = 1

