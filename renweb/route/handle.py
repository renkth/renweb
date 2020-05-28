#!/usr/bin/env python
# -*- coding: utf-8 -*-


from renweb.http.utils import jsonify
from renweb.modle.query import Query

@jsonify
def hello(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        passwd = request.POST.get("pw")
    elif request.method == 'GET':
        email = request.GET.get("email")
        passwd = request.GET.get("pw")

    user = Query().get_user(email,passwd)
    # print user.values()
    return user.getvalues()
    # return ("hello world!{},{}".format(email,passwd))
