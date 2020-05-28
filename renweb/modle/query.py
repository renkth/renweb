#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core import with_um

class Query(object):
    # def __init__(self,request):
    #     self.request = request

    @with_um
    def get_user(self,phone,fee_app_code):
        return self.um.get(phone,fee_app_code)


if __name__ == "__main__":
    Query(None)