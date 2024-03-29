#!/usr/bin/env python3

'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/9/26 9:50
@Software: PyCharm
@File    : mysession.py
'''
from uuid import uuid4

from day5.util.myutil import myuuid

s = {"128位uuid":{'k1':'v1','k2':'v2'},"128位uuid":{'k1':'v1','k2':'v2'},}

class Session:
    def __init__(self,handler):
        self.handler = handler

    def __getitem__(self, key):
        # print("Session的getitme方法被触发，key是",key)
        c= self.handler.get_cookie('uid')
        if c:
            d = s.get(c)
            if d:
                return d.get(key)
            else:
                return None
        else:
            return None

    def __setitem__(self, key, value):
        # print("Session的setitme方法被触发，key是",key,'value是',value)
        c = self.handler.get_cookie('uid')
        if c:
            d = s.get(c,None)
            if d:
                d[key] = value
            else:
                d = {}
                d[key] = value
                s[c] = d
        else:
            u = myuuid(uuid4())
            d = {}
            d[key] = value
            s[u] = d
            self.handler.set_cookie('uid',u,expires_days=10)


# s = Session()
# s['a'] = 'b'
# print(s['a'])
