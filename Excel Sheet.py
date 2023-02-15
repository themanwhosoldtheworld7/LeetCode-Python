#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:10:40 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/excel-sheet-column-number/

https://leetcode.com/problems/excel-sheet-column-title/

"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        alphabet = {chr(65+i):i+1 for i in range(26)}
        alphabet["Z"] = 26
        exp = 0
        col = 0

        for i in range(len(s)-1, -1, -1):
            col = col + alphabet[s[i]] * 26**exp
            exp+=1
        return col
    
    dicty={i:chr(65+i) for i in range(26)}
    
    def convertToTitle(self, columnNumber: int) -> str:
        i=0
        while True:
            if columnNumber-26**i<0:
                i-=1
                break
            columnNumber-=26**i
            i+=1
        res=""
        for j in range(i,-1,-1):
            res=res+self.dicty[columnNumber//(26**j)]
            columnNumber-=26**j*(columnNumber//(26**j))
        return res