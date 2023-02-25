#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 11:15
# @Author  : Arrow and Bullet
# @FileName: app.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41800366
import logging  # 导入logging模块
from aiohttp import web

logging.basicConfig(level=logging.INFO)  # 配置logging的基本信息， level=logging.INFO,记录INFO及以上的日志


def index(request):
    return web.Response(body='<h1>AWesome</h1>'.encode('utf-8'), content_type='text/html')


def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    web.run_app(app, host='127.0.0.1', port=9000)
    logging.info('server started at http://127.0.0.1:9000...')


init()
