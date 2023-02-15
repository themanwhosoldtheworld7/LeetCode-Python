#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:37:38 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/max-consecutive-ones-ii/
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left, right, zeros = 0,0,0
        longest = 1
        while right < len(nums):
            if nums[right] == 0:
                zeros+=1
            
            while zeros == 2:
                if nums[left] == 0:
                    zeros -=1
                left+=1
            
            longest = max(longest, right - left +1 )
            right+=1
        return longest
        