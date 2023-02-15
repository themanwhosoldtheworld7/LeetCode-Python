#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:00:24 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/isomorphic-strings/
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        for i, j in zip(s, t):
            try:
                if d1[i] != j:
                    return False
            except:
                d1[i] = j
        
        d1 = {}
        for j,i in zip(s, t):
            try:
                if d1[i] != j:
                    return False
            except:
                d1[i] = j
        
        return True