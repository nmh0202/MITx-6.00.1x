#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:41:00 2017

@author: nmh0202
"""
s = 'azcbobobegghakl'
count = 0
for i in s:
    if i  =='a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
print (count)