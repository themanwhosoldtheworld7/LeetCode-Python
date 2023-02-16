#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:16:57 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n=len(s)
        m=len(p)
        if m > n: return []
        
        base   = [0]*26
        string = [0]*26
        result = []
        i, j   = 0,0
        
        # Setup frequency map for base string
        for c in p:
            base[ord(c)-97] +=1


        
        while i<=n-m and j <m:
            c  = ord(s[i+j]) - 97
            fc = ord(s[i])   - 97         
            # if c does not exist in base string
            #reset J, reset string map
            if base[c] == 0:
                i = i+j+1
                j = 0
                string = [0]*26
                continue
            
            string[c] += 1
            j += 1
            
            if j == m:
                if base == string:
                    result.append(i)
                string[fc]-=1
                j-=1
                i+=1

        return result