#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:29:31 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/longest-common-prefix/
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        prefix = ""
        
        for a in zip(*strs):
            if len(a) == 1:
                prefix += a[0]
            else:
                return prefix
        return prefix