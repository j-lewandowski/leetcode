# https://leetcode.com/problems/longest-common-prefix/
from typing import List

class Solution:
    def LCP(self, a: str, b: str):
        i = 0
        result = ""
        while i <= len(a) and i <= len(b):
            if a[:i] != b[:i]:
              break
            result = a[:i]
            i += 1
        return result
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        result = self.LCP(strs[0], strs[1])
        for i in range(2, len(strs)):
            result = self.LCP(result, strs[i])
        return result
        
        
        

# print(Solution().longestCommonPrefix(["flower","flow","flight"]))
# print(Solution().longestCommonPrefix(["dog","racecar","car"]))
# print(Solution().longestCommonPrefix(["ab","a"]))