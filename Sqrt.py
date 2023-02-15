#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:19:03 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/sqrtx/
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        while(low<=high):
            mid=low+(high-low)//2
            if (mid*mid<=x and (mid+1)*(mid+1)>x):
                return mid
            elif mid*mid<x:
                low=mid+1
            else:
                high=mid-1
        return low