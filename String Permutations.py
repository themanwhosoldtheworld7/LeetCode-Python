#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:20:50 2023

@author: Themanwhosoldtheworld

https://leetcode.com/problems/permutation-in-string/
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        # if s1 got more characters, 
        # then s2 can never contain a permutation of s1
        if n > m: return False
        # cnt_s1: frequency of character in s1
        # cnt_s2: frequency of character in s2
        cnt_s1, cnt_s2 = [0] * 26, [0] * 26
        # count the frequency of characters in s1 first
        for i in range(n):
            cnt_s1[ord(s1[i]) - ord('a')] += 1
        # for each character in s2
        for i in range(m):
            # we increase the frequency in cnt_s2
            cnt_s2[ord(s2[i]) - ord('a')] += 1
            # given the window size `n`,
            # if the current index >= n, it means we need to pop the leftmost element out
            # e.g. window size = 2 - now it includes `eid` - we need to pop `e` out
            if i >= n: cnt_s2[ord(s2[i - n]) - ord('a')] -= 1
            # check if both frequency count matches or not
            if cnt_s1 == cnt_s2: return True
        return False