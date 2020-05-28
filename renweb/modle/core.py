#!/usr/bin/env python
# -*- coding: utf-8 -*-
from helper import SubManager

def with_um(func):
    def wapper(self,*args,**kw):
        self.um = SubManager()
        try:
            return func(self,*args,**kw)
        except:
            raise
        finally:
            self.um.close()
            del self.um
    return wapper