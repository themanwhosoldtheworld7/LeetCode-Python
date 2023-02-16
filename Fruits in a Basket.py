#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:06:35 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/fruit-into-baskets/
"""
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        
        n = len(fruits)
        if n<3:
            return n
        
        basket = set(fruits)
        if len(basket) < 3:
            return len(fruits)
        
        basket = {fruits[0], fruits[1]}
        i, count, maxcount = 2,2,2             
        


        while(i < n):
            
            if len(basket) <= 2:
                basket.add(fruits[i])
                count+=1
                i+=1
            
            if len(basket) == 3:
                count-=1
                i = i-1
                maxcount = max(count, maxcount)
                count    = 0
                basket.remove(fruits[i])
                basket.remove(fruits[i-1])
                i = i-1
                
                while (fruits[i] not in basket):
                    i -=1
                i+=1
                basket = set()
        
        return max(maxcount, count)