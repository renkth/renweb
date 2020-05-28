#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from datetime import datetime,date
# import datetime.date


class Response(object):
    def __init__(self,data,body):
        self.data = data
        self.body = body
        self.headers = [
            ('Content-type', 'text/plain'),
            ('Content-Length', '%s' % len(self.body)),
        ]
        self.status = '200 OK'

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.body

class DateEncoder(json.JSONEncoder):
    """
    解决json序列化时时间不能序列化问题
    例:json.dumps(data, cls=DateEncoder)
    """
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')

        else:
            return json.JSONEncoder.default(self, obj)

def jsonify(func):
    def wapper(request):
        res = func(request)
        type(res)
        if isinstance(res, dict):
            return Response(res, json.dumps(res,cls=DateEncoder))
        return Response(res, res)
    return wapper










