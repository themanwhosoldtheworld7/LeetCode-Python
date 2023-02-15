#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:15:02 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/rotate-image/
"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #1. Transpose Matrix
        #2. Flip Matrix
        
        l = len(matrix)
        for i in range(l):
            for j in range(i,l):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
     
        k = 0
        while (i>k):
            for j in range(l):
                matrix[j][i], matrix[j][k] = matrix[j][k], matrix[j][i]
            i-=1 
            k+=1
        return matrix