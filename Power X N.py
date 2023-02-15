#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:15:31 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/powx-n/

Solved using Dynamic programming. 

When the power is divisible by 2, we square the numnber, else we cube the number
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (x == 1 or n==0):
            return 1
        
        if n<0: x=1/x
        result = self.power(x, abs(n))
        return result
    
    def power(self, x, n):
        if n == 1: return x
        result = self.power(x, n//2)

        if n%2 == 0: return result * result
        if n%2 ==1:  return result * result * x