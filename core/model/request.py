#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : request.py
 @Time       : 2021/2/12 12:40
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2021, iFuture Corporation Limited.
"""
from datetime import datetime
from dataclasses import dataclass, field
from configs.constant import GET, HTML
from utils.color import Colored
from typing import List, Dict, Union, Any


@dataclass
class StopCondition(object):
    name: str
    min_value: Union[int, datetime]
    max_value: Union[int, datetime]
    evaluation: str
    step: int  # 数字或者天数


@dataclass
class RequestTemplate(object):
    request_id: int
    start_url: Union[List[str], str]
    method: str = GET
    post_data: str = None
    extra_headers: Dict[str, str] = field(default_factory=dict)
    referer: str = None
    process: str = None
    parameters: str = None
    timeout: int = 20
    sleep_time: float = 0.5
    need_render: bool = False
    use_proxy: bool = False
    cookies: str = None
    use_session: bool = True
    is_duplicate: bool = False
    result: str = None
    return_type: str = HTML
    return_item: str = None
    stop_by: List[StopCondition] = None

    def __str__(self):
        return Colored.yellow(f"[{self.request_id}] <Request [{self.method}] [{self.start_url}]>")

    def __contains__(self, item):
        return True if item.request_id == self.request_id else False
