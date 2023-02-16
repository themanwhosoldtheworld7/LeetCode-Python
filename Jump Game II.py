#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:05:17 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/jump-game-ii/
"""
class Solution:
    def jump(self, nums: list[int]) -> int:
        N = len(nums)
        Solutions = [float('inf')] * N
        Solutions [N-1] = 0
            
        for i in range(N-2, -1, -1):
            for j in range (1, min(nums[i]+1,N)):
                if i + j < N:
                    Solutions[i] = min (Solutions[i], Solutions[i+j]+1)
        return Solutions[0]