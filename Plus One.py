#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:27:34 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/plus-one/
"""
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[len(digits)-1] !=9:
            digits[len(digits)-1]+=1
            return digits
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
        digits.insert(0,1)
        return digits