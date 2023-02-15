#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:21:41 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/group-anagrams/
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        result = {}
        for s in strs:
            ss = "".join(sorted(s))
            
            try:
                result[ss].append(s)
            except:
                result[ss] = [s]
                
        result = list(result.values())
        
        return result

