#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '80022068'
__mtime__ = '2019/8/19'
# qq:2456056533


"""
import os
from loguru import logger as klogger

LOG_DIR = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

klogger.add(
    os.path.join(LOG_DIR, '{time:YYYY-MM-DD}.log'),
    format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}',
    enqueue=True,
    rotation='500 MB',
    retention='7 days',
    encoding='utf-8'
)
