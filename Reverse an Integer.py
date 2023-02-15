#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:33:30 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x: int) -> int:
        if -9<=x and x<=9:
            return x
        sign = 1
        if x<0:
            sign = -1
        
        x = abs(x)
        reverse = 0
        while (x>=1):
            digit = x%10
            x = x//10
            reverse = reverse*10 + digit
        
        A = bin(reverse)
        if len(A) > 33:
            reverse = 0      
        return reverse * sign