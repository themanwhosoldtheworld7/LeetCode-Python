#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:18:18 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/climbing-stairs/

https://leetcode.com/problems/fibonacci-number/
"""
class Solution:
    def climbStairs(self, n):           
        if n in [0,1]: return 1
        n1, n2 = 1,1 
        for i in range(1,n):
            n1, n2 = n2, n1+n2
        return n2