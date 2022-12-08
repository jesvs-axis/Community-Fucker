#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# nome   : Email OSINT
# url creator    : https://github.com/jesvs-axis
# creator : Axis

from setuptools import setup 

setup(
    name='infoga',

    version='0.1.5',
    description='Email OSINT',
    url='https://github.com/jesvs-axis',
    
    author = 'Axis',
    license='GPLv3',

    install_requires = ['colorama','requests','urllib3'],
    console =['infoga.py'],
)