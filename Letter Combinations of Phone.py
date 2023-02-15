#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:26:39 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

class Solution:
    letters = {     '2': ['a','b','c'],
                    '3': ['d','e','f'],
                    '4': ['g','h','i'],
                    '5': ['j','k','l'],
                    '6': ['m','n','o'],
                    '7': ['p','q','r','s'],
                    '8': ['t','u','v'],
                    '9': ['w','x','y', 'z'] }
    
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        
        combinations = []
        def CreateCombinations (depth, current):
            if len(current) == len(digits):
                combinations.append(current)
                return
            
            for letter in self.letters[digits[depth]]:
                CreateCombinations(depth+1, current + letter)
        
        CreateCombinations (0,'')        
        return combinations