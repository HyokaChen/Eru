#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : db.py
 @Time       : 2021/11/14 23:01
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2021, iFuture Corporation Limited.
"""
import redis
from configs.constant import (REDIS_PWD, REDIS_HOST, REDIS_PORT)

_pool = redis.ConnectionPool(max_connections=5000, host=REDIS_HOST, port=REDIS_PORT, socket_timeout=10,
                             retry_on_timeout=10, password=REDIS_PWD, db=0)
redis_db = redis.StrictRedis(connection_pool=_pool)


__all__ = [
    'redis_db'
]
