#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : constant.py
 @Time       : 2021/2/12 12:12
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2021, iFuture Corporation Limited.
"""
import os
import sys
from enum import Enum, unique
from envparse import env


@unique
class StatusType(Enum):
    NONE = 0
    SUCCESS = 1
    FAIL = 2


env.read_envfile('~/.env')
# 配置文件
POSTGRESQL_HOST = env('POSTGRESQL_HOST')
POSTGRESQL_PORT = env.int('POSTGRESQL_PORT')
POSTGRESQL_USER = env('POSTGRESQL_USER')
POSTGRESQL_PWD = env('POSTGRESQL_PWD')
POSTGRESQL_DB = env('POSTGRESQL_DB')
REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env.int('REDIS_PORT')
REDIS_PWD = env('REDIS_PWD')
TEMPLATE_PATH = env('TEMPLATE_PATH')

# 模板解析字段
REQUESTS_DOT = 'REQUESTS.'
PROCESSES_DOT = 'PROCESSES.'
RESULTS_DOT = 'RESULTS.'
DOT = '.'
DOLLAR = '$'
AND = '&'
AT = '@'
HASH = '#'
DIAGONAL = '//'
GREATER_THAN = '>'
LESS_THAN = '<'
UNDER_LINE = '_'
LEFT_BRACE = '{'
RIGHT_BRACE = '}'
LEFT_BRACKET = '['
RIGHT_BRACKET = ']'
PERCENT = '%'
COLON = '::'
HALF_COLON = ':'
TRANSFORM_TO = '->'

# 解析内容类型
TEXT = "text"
CSS = 'css'
JSON = "json"
HTML = "html"
LIST = 'list'
ONE = 'one'
GET = 'GET'
POST = 'POST'

# 排除字段
EXCLUDE_FIELD = {"id", "insert_time", "timestamp",
                 "global_parameter",
                 "result_id", "process_id",
                 "template_id"}

# 类型转换
TYPE_FUNC_MAP = {
    'int': int,
    'list': list,
    'str': str,
    'default': str
}

# 时间格式
DAILY_FORMAT = "%Y-%m-%d"
DATE_FMT = '%Y-%m-%d %H:%M:%S'
ES_DATE_FMT = '%Y-%m-%dT%H:%M:%S.000Z'

# 消息队列
# 'task_{stream}-{hash_id}'
REQUESTS = 'REQUESTS'
PROCESSES = 'PROCESSES'
RESULTS = 'RESULTS'
DOWNLOAD_STREAM = 'download_stream'
PROCESS_STREAM = 'process_stream'
RESULT_STREAM = 'result_stream'
MAX_LEN = 2000

# 类别
NEWS = 'news'
MUSIC = 'music'
VIDEO = 'video'
IMAGE = 'image'
WEIBO = 'weibo'
QZONE = 'qzone'

# 推送
PUBLISHED = "article-{0}-node"

# 解析方式
XPATH_EXTRACTOR = 'xpath'
CSS_EXTRACTOR = 'css'
JSON_EXTRACTOR = 'json'
FUNCTION_EXTRACTOR = 'function'
REDIS_EXTRACTOR = 'redis'
EXECUTE_EXTRACTOR = 'execute'
FORMAT_EXTRACTOR = 'format'
REGEX_EXTRACTOR = 'regex'
REPLACE_EXTRACTOR = 'replace'
RESPONSE_EXTRACTOR = 'response'

NATIONALITY = {
    '': '未知',
    '1': '中国',
    '2': '中国台湾',
    '3': '中国香港',
    '4': '日本',
    '5': '韩国',
    '6': '美国',
    '7': '英国',
    '8': '德国',
    '9': '法国',
    '10': '印度',
    '11': '瑞典',
    '12': '挪威',
    '13': '朝鲜',
    '14': '越南',
    '15': '伊朗',
    '16': '古巴',
    '17': '希腊',
    '18': '巴西',
    '19': '捷克',
    '20': '泰国',
    '21': '波兰',
    '22': '荷兰',
    '23': '南非',
    '24': '意大利',
    '25': '奥地利',
    '26': '新西兰',
    '27': '墨西哥',
    '28': '俄罗斯',
    '29': '西班牙',
    '30': '新加坡',
    '31': '牙买加',
    '32': '马来西亚',
    '33': '澳大利亚',
    '34': '哥伦比亚',
    '35': '罗马尼亚',
    '40': '加拿大',
    '41': '塞尔维亚',
    '42': '格鲁吉亚',
    '43': '老挝',
    '44': '不丹',
    '45': '孟加拉',
    '46': '乌克兰',
    '47': '丹麦',
    '48': '缅甸',
    '49': '土耳其',
    '50': '比利时',
    '51': '瑞士',
    '52': '阿根廷',
    '53': '斯里兰卡',
    '54': '阿拉伯',
    '55': '匈牙利',
    '56': '智利',
    '57': '印度尼西亚',
    '58': '爱尔兰',
    '59': '菲律宾',
    '60': '尼日利亚',
    '61': '波多黎各',
    '62': '多米尼加共和国',
    '63': '尼泊尔',
    '64': '叙利亚',
    '65': '埃塞俄比亚',
    '66': '巴基斯坦',
    '68': '委内瑞拉',
    '69': '保加利亚',
    '70': '阿塞拜疆',
    '71': '以色列',
    '72': '贝宁',
    '73': '巴巴多斯',
    '74': '阿尔及利亚',
    '75': '芬兰',
    '76': '秘鲁',
    '77': '葡萄牙',
    '78': '立陶宛',
    '79': '埃及',
    '80': '蒙古',
    '81': '爱沙尼亚',
    '82': '波黑',
    '83': '斯洛伐克'
}

ASTROLOGY = {
    '': '未知',
    '1': '白羊座',
    '2': '金牛座',
    '3': '双子座',
    '4': '巨蟹座',
    '5': '狮子座',
    '6': '处女座',
    '7': '天秤座',
    '8': '天蝎座',
    '9': '射手座',
    '10': '摩羯座',
    '11': '水瓶座',
    '12': '双鱼座'
}

