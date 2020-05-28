#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urlparse import unquote
import uuid

from renweb.route.urls import patterns

def parseQueryString(query):
    if not query:
        return {}
    dict = {}
    for p in query.split("&"):
        try:
            k,v = p.split("=")
            if v!='':
                dict[k.lower()] = unquote(v.replace('+', ' '))
        except ValueError:
            pass
    return dict




class Request(object):
    def __init__(self, environ):
        self.environ = environ
        self.method = environ['REQUEST_METHOD']
        self.queryString = environ['QUERY_STRING']
        self.serverName = environ['SERVER_NAME']
        self.serverPort = environ['SERVER_PORT']
        self.remoteHost = environ['REMOTE_ADDR']
        self.GET = parseQueryString(environ['QUERY_STRING'])
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        self.POST = parseQueryString(environ["wsgi.input"].read(request_body_size))


def newSID():
    return str(uuid.uuid4()).replace('-', '')[::2]

def serve(settiings):
    urls = patterns

    def application(environ, start_response):
        path = environ['PATH_INFO']
        handler = None
        for url in urls:
            if url[0] == path:
                handler = url[1]
        if not handler:
            status = '404 Not Found'
            response_headers = [('Content-type', 'text/plain'),
                                ('Content-Length', '0')]
            start_response(status, response_headers)
            return ['']



        request = Request(environ)
        request.sid = newSID()
        response = handler(request)
        # response = Response(rs, rs)
        # response = handler(request)
        start_response(response.status, response.headers)
        return [str(response)]

    return application