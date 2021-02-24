#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'stringk'
__mtime__ = '2020/8/7'
# qq | WX:2456056533

佛祖保佑  永无bug!

"""

import uvicorn
from fastapi import Request
from fastapi.responses import JSONResponse

from app.log import klogger

from app.app import create_app

app = create_app()


@app.exception_handler(Exception)
async def app_exception(request: Request, exc: Exception):
    '''拦截所有未知 非HTTPException 异常'''
    klogger.info('Request url:{}'.format(request.url))
    klogger.info('Request path_params:{}'.format(request.path_params))
    klogger.info('Request query_params:{}'.format(request.query_params))
    klogger.info('Request exception:{}'.format(exc))

    return JSONResponse({
        "error_code": 99999,
        "msg": 'sorry for error:{}'.format(exc),
        "data": {},
    }, status_code=500)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=40000, debug=False)
    # uvicorn --host 0.0.0.0 --port 40000 manager:app
