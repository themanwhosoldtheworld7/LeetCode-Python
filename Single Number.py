#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:12:27 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/single-number/
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Solved using XOR Gates
        """
        a = 0
        for i in nums:            
            a ^= i
        return a