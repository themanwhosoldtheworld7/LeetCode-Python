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
        maxlength = 0
        length = 0
        maxlength = 0
        
        for i in range(len(s)):
            try:
                l = location[s[i]]
                maxlength = max(length, maxlength)
                length = i - l
                location[s[i]]=i
                
            except:
                location[s[i]] = i
                length+=1
        
        return max(length, maxlength)