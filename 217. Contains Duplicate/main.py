# https://leetcode.com/problems/contains-duplicate/description/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set()
        for num in nums:
            if num in unique_elements:
                return True
            else:
                unique_elements.add(num)
        return False
