#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class global_var:
    getpriv = False
def set_priv(status):
    global_var.getpriv = status
def get_priv():
    return global_var.getpriv