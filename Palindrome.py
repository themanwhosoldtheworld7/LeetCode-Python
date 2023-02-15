#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:34:09 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/palindrome-number/
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        num = 0
        multiplier = 10
        
        while x>=1:
            digit = x % 10
            x = x//10
            num = num * multiplier + digit  
        return num == y