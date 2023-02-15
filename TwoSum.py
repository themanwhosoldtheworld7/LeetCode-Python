#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:35:49 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/two-sum/

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        Targets = {}
        
        for i in range(len(nums)):
            try:
                j = Targets[target - nums[i]]                
                return [j,i]
            except:
                Targets[nums[i]] = i
        return