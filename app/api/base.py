#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'stringk'
__mtime__ = '2021/1/18'
# qq | WX:2456056533

佛祖保佑  永无bug!

"""
import time
from typing import Optional

from fastapi import APIRouter
from app.log import klogger

ai_router = APIRouter()


@ai_router.get('/time')
async def index():
    '''k8s 探针 http监控服务请求地址'''
    return {'error_code': 0, 'msg': 'success', 'data': {'time': time.strftime('%Y-%m-%d-%H-%M', time.localtime())}}


@ai_router.get('/')
async def tf_gpu_check(q: Optional[str] = None):
    if q == 'tf':
        import tensorflow as tf
        from tensorflow.python.client import device_lib
        klogger.info('check tensorflow use GPU...')

        tf_is_gpu_available = tf.test.is_gpu_available()
        klogger.info('tf.test.is_gpu_available:{}'.format(tf_is_gpu_available))

        tf_gpu_device_name = str(tf.test.gpu_device_name())
        if not tf_gpu_device_name:
            tf_gpu_device_name = ''

        klogger.info('tf.test.gpu_device_name:{}'.format(tf_gpu_device_name))

        tf_is_built_with_cuda = tf.test.is_built_with_cuda()
        klogger.info('tf.test.is_built_with_cuda:{}'.format(tf_is_built_with_cuda))

        local_device_protos = device_lib.list_local_devices()
        gpu_devices = [str(x) for x in local_device_protos if x.device_type == 'GPU']
        klogger.info('device_lib.list_local_devices:{}'.format(gpu_devices))

        return {'tf_is_gpu_available': tf_is_gpu_available, 'tf_gpu_device_name': tf_gpu_device_name,
                'tf_is_built_with_cuda': tf_is_built_with_cuda, 'gpu_devices': gpu_devices}

    elif q == 'keras':
        klogger.info('check keras use GPU...')

        try:
            from tensorflow.python.keras.backend import _get_available_gpus
        except Exception as e:
            klogger.info('import error:{}'.format(e))
            from keras.backend.tensorflow_backend import _get_available_gpus

        from tensorflow.python.client import device_lib

        local_device_protos = device_lib.list_local_devices()
        gpu_devices = [str(x) for x in local_device_protos if x.device_type == 'GPU']
        klogger.info('device_lib.list_local_devices:{}'.format(gpu_devices))

        keras_get_available_gpus = [str(x) for x in _get_available_gpus()]
        klogger.info('keras get_available_gpus:{}'.format(keras_get_available_gpus))

        return {'gpu_devices': gpu_devices, 'keras_get_available_gpus': keras_get_available_gpus}


    elif q == 'torch':
        import torch
        klogger.info('check torch use GPU...')

        cuda_device_count = torch.cuda.device_count()
        klogger.info('torch.cuda.device_count:{}'.format(cuda_device_count))

        cuda_is_available = torch.cuda.is_available()
        klogger.info('torch.cuda.is_available:{}'.format(cuda_is_available))

        try:
            cuda_current_device = str(torch.cuda.current_device())
            klogger.info('torch.cuda.current_device:{}'.format(cuda_current_device))

            device = str(torch.device('cuda:0' if cuda_is_available else 'cpu'))
            klogger.info('device :{}'.format(device))

        except Exception as e:
            klogger.info('error:{}'.format(e))
            raise e

        return {'cuda_device_count': cuda_device_count, 'cuda_is_available': cuda_is_available, 'device': device,
                'cuda_current_device': cuda_current_device}

    return {'demo': 'http://host:ip/?q=tf2', 'list': ['tf', 'keras', 'torch']}
