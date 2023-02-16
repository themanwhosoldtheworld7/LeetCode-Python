#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:42:13 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/third-maximum-number/
"""

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        largest = []
    
        for element in nums:
            if element in largest:
                continue

            if len(largest) <3:
                largest.append(element)
                largest.sort()
                continue       

            if element < largest[0]:
                continue

            largest.pop(0)
            largest.append(element)
            largest.sort()

        if len(largest)<3:
            return largest[-1]
        return largest[0]        