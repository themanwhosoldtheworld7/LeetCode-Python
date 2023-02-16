#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:04:01 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/first-unique-character-in-a-string/
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==1:
            return 0
        repeats = [0] * 26
        letters = {}
        i = -1
        
        for letter in s:
            i+=1
            place = ord(letter)-97
            if repeats[place] != 0:
                continue
            
            try:
                del letters[letter]
                repeats[place] = 1
            except:
                letters[letter] = i
        
        if len(letters) == 0:
            return -1
        
        return letters [ list(letters.keys())[0]]