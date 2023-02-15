#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:39:37 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result = []
        
        for i in range(len(nums)):
            #make number at index nums[i] negetive to use as flag
            index = abs(nums[i])-1
            if nums[index] > 0: nums[index]=nums[index]*-1
        
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(i+1)
        
        
        return result
        