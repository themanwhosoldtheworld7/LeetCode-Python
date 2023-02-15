#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:30:56 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/zigzag-conversion/
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        downward = list(range(numRows))
        upward   = list(range(numRows-2,0, -1))
        ZigZag   = (downward+upward)
        
        Pattern  = ZigZag * int(((len(s)/len(ZigZag))+1))
        strings = ["" for _ in range(len(ZigZag))] 
        
        for row,char in zip(Pattern, s):
            strings[row] += char
        
        return "".join(strings).rstrip()