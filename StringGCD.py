#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:36:48 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 != str2+str1:
            return ""        
        length = math.gcd(len(str1), len(str2))
        return str1[:length]