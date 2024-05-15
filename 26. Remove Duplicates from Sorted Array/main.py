# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        i = 1
        while i < len(nums):
            if nums[i] == "_":
                break
            if nums[i] == nums[i - 1]:
                counter += 1
                nums.pop(i)
                nums.append("_")
            else:
                i += 1
        return len(nums) - counter


print(Solution().removeDuplicates([1, 1, 2]))
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
