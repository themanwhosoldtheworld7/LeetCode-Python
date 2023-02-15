#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:34:58 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/verifying-an-alien-dictionary/
"""

class Solution:

    
    def isAlienSorted( self, words, order):
        LexIndex = {}
        
        for i in range(len(order)):
            LexIndex[order[i]] = i
            
        for word1, word2 in zip(words, words[1:]):
            #check for fullsubstring
            if (len(word1) > len(word2) and word1[:len(word2)]==word2):
                return False

            for c1, c2 in zip(word1, word2):
                if LexIndex[c1] < LexIndex[c2]:
                    break
                elif LexIndex[c1] > LexIndex[c2]:
                    return False
                
        return True