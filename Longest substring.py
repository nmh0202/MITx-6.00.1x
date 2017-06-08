#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 18:39:53 2017

@author: nmh0202
"""
s = 'azcbobobegghakl'
ans = s[0]
res = s[0]
for i in range(1,len(s)):   
    if s[i] >= s[i-1]:
        ans = ans + s[i]
        if len(res) < len(ans):
            res=ans
    elif s[i] < s[i-1]:
        ans =s[i]
print (res)