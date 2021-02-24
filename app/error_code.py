#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'stringk'
__mtime__ = '2020/8/25'
# qq | WX:2456056533

佛祖保佑  永无bug!

"""
from typing import Optional, Dict, Any

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


# class UnicornException(Exception):
#     def __init__(self, error_code=500, data={}, msg=''):
#         self.error_code = error_code
#         self.msg = msg
#         self.data = data
#
#
# async def unic_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         content={
#             "error_code": exc.error_code,
#             "msg": exc.msg,
#             "data": exc.data,
#         },
#         status_code=400,
#     )
#

class ApiException(HTTPException):
    status_code: int = 500  # 响应状态码
    error_code: int = 10000  # 错误状态码
    data: dict = {}
    msg: str = 'server error'
    headers: Optional[Dict[str, Any]] = None

    def __init__(self, status_code=None, error_code=None, data=None,
                 msg=None, headers=None):
        if status_code:
            self.status_code = status_code
        if error_code:
            self.error_code = error_code
        if data:
            self.data = data
        if msg:
            self.msg = msg

        if headers:
            self.headers = headers

        super(ApiException, self).__init__(
            status_code=self.status_code, detail=self.msg, headers=self.headers
        )

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r},error_code={self.error_code!r}, msg={self.msg!r}),data={self.data!r}"


async def api_exception_handler(_: Request, exc: ApiException) -> JSONResponse:
    return JSONResponse({
        "error_code": exc.error_code,
        "msg": exc.msg,
        "data": exc.data
    }, status_code=exc.status_code)


# 9980-9989
class ParameterException(ApiException):
    '''参数异常'''
    status_code = 400
    error_code = 9980
    msg = 'invalid parameter'


# 9970-9979
class FileException(ApiException):
    '''文件异常'''
    status_code = 400
    error_code = 9970
    msg = 'file error'


# 9960-9969
class TokenException(ApiException):
    status_code = 400
    error_code = 9960
    msg = 'token error'


# 9950-9959
class UploadImgException(ApiException):
    status_code = 400
    error_code = 9950
    msg = 'upload error'


class TimeoutException(ApiException):
    status_code = 400
    error_code = 9940
    msg = 'timeout'


# 8000-8999
class AlgException(ApiException):
    status_code = 400
    error_code = 8000
    msg = 'alg exception'


if __name__ == '__main__':
    per = ParameterException(msg='缺少img_url参数')
    print(per.status_code)
    print(per.error_code)
    print(per.msg)

    ap = ApiException()
    print(ap.status_code)
    print(ap.error_code)
    print(ap.msg)
