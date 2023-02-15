#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:38:53 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/squares-of-a-sorted-array/
"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [] 
        left, right = 0,len(nums)-1
        
        while (right > left):
            if (abs(nums[right]) < abs(nums[left])):
                result.insert(0, nums[left]*nums[left])
                left+=1
                continue
            result.insert(0,nums[right]*nums[right])
            right = right -1
        result.insert(0, nums[right]*nums[right])
        return result