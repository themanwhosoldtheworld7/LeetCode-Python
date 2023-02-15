#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:45:30 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""

class Solution:    
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for element in nums:
            if len(str(element))%2 == 0:
                count+=1
        return count