#!/usr/bin/env python
# -*- coding: utf-8 -*-
from renweb.route.handle import hello
patterns = {
    # query
    ('/hello', hello)
}