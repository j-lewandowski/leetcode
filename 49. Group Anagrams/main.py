# https://leetcode.com/problems/group-anagrams/description/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in groups:
                groups[s_sorted].append(s)
            else:
                groups[s_sorted] = [s]
        return list(groups.values())
