#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'stringk'
__mtime__ = '2021/1/18'
# qq | WX:2456056533

佛祖保佑  永无bug!

"""
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from app.error_code import ApiException, api_exception_handler

APP_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.dirname(APP_DIR))


def create_app() -> FastAPI:
    app = FastAPI(title='ai-service', default_response_class=ORJSONResponse)

    # 事件处理
    # app.add_event_handler('startup',start_app_handler(app))
    # app.add_event_handler('shutdown', stop_app_handler(app))

    # 错误处理
    app.add_exception_handler(ApiException, api_exception_handler)
    # app.add_exception_handler(UnicornException, unic_exception_handler)

    init_middlewares(app)
    register_router(app)
    return app


def register_router(app: FastAPI):
    from app.api.base import ai_router
    app.include_router(ai_router)


def init_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
