#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:28:57 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/length-of-last-word/
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = len(s)
        while ( i>=0 ):
            i-=1
            if s[i] == " ":
                return len(s)-i-1
        return len(s)