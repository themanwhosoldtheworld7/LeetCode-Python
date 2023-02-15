#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:08:15 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/happy-number/
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        if n ==1: return True
        if n in [2,3]: return False
        
        end = False
        result = 0
        previous = []
        
        while end == False:
            result = 0
            while n>0:
                result = result + (n%10)**2
                n = n//10
            if result == 1: return True
            if result in previous: return False    
            previous.append(result)
            n = result