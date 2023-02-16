#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:31:20 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        location = {}
        count    = 0
        maxcount = 0
        i = 0
        while i < len(s):
            try:
                    l = location[s[i]]
                    maxcount = max(count, maxcount)
                    count = 0
                    i = l+1
                    location = {}
            except:
                location[s[i]] = i
                count+=1
                i+=1
        return max(count, maxcount)