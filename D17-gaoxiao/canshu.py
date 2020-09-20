#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 10:36
# @Author  : Aries
# @Site    : 
# @File    : 01-excleTest1.py
# @Software: PyCharm
'''


dict1={'first':False,'pn':2,'kd':'自动化测试工程师'}

def setSHEzhui(pn=None,kd=None):
	data=dict1
    data['pn']=pn
    data['kd']=kd
	return data

#设计接口用例

def test_001():
	'''pn为空'''
	setShezhi(kd='性能测试')

def test_002():
	'''kd为空'''
	setShezhi(pn=2)

def test_003():
	'''都为空'''
	setShezhi()