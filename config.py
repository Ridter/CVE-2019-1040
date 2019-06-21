#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class global_var:
    getpriv = False
    user = ""
    restore = ""
    ntlm = ""
def set_priv(status):
    global_var.getpriv = status
def get_priv():
    return global_var.getpriv

def set_user(user):
    global_var.user = user

def get_user():
    return global_var.user

def set_restore(rfile):
    global_var.restore = rfile
def get_restore():
    return global_var.restore

def set_ntlm(ntlm):
    global_var.ntlm = ntlm
def get_ntlm():
    return global_var.ntlm