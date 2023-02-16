#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:29:57 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    E2R = { 
            0:{1:"", 10:"", 100:"", 1000:""},    
            1:{1:"I", 10:"X", 100:"C", 1000:"M"},
            2:{1:"II", 10:"XX", 100:"CC", 1000:"MM"},
            3:{1:"III", 10:"XXX", 100:"CCC", 1000:"MMM"},
            4:{1:"IV", 10:"XL", 100:"CD", 1000:"M"},
            5:{1:"V", 10:"L", 100:"D"},
            6:{1:"VI", 10:"LX", 100:"DC", },
            7:{1:"VII", 10:"LXX", 100:"DCC",},
            8:{1:"VIII", 10:"LXXX", 100:"DCCC",},
            9:{1:"IX", 10:"XC", 100:"CM", },
            
          }
    
    R2E = {
          "I":1,
          "V":5,
          "X":10,
          "L":50,
          "C":100,
          "D":500,
          "M":1000
          }
    
    def intToRoman(self, num: int) -> str:        
 
        num2 = num
        place = 1
        RN = ""
        
        while num2 >=1:            
            digit = num2%10            
            RN = self.E2R[digit][place] + RN
            place = place*10
            num2 = num2//10
        return RN
    
    def romanToInt(self, s:str) -> int: 
        arabic = 0
        ar = 0
        i=len(s)
        while (i>0):
            i-=1
            ar = self.R2E [s[i]] if self.R2E[s[i]] >= ar else -self.R2E[s[i]]
            arabic = arabic+ar
        return arabis