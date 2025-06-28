# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        frequency = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for n, c in counter.items():
            frequency[c].append(n)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res