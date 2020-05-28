#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from renweb import config as settings
from renweb.http import serve

application = serve('a')

if __name__ == "__main__":

    from wsgiref.simple_server import make_server

    httpd = make_server('', 8000, application)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()