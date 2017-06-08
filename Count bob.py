#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:49:46 2017

@author: nmh0202
"""
#s = 'azcbobobegghakl'
#s = 'oeaobobbobobboboboboobobouboboobobobo'
s = 'ybobobboobobhanbobyobob'
# Paste your code into this box 
c=0
for i in range(len(s)-2):
    if s[i] == 'b' and s[i+1] =='o' and s[i+2] == 'b':     
        c+=1
print ('Number of times bob occurs is: '+ str(c))
            