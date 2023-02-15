#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:43:04 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/height-checker/
"""

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count+=1
        return count
        