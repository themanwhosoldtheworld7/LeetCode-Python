#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:47:22 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/detect-capital/
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() == True:
            return True
        if word.islower() == True:
            return True
        if word[1:].islower() == True:
            return True
        return False