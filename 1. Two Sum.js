// https://leetcode.com/problems/two-sum/description/

function twoSum(nums, target) {
  const hashmap = {};

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (target - num in hashmap) {
      return [i, hashmap[target - num]];
    }
    hashmap[num] = i;
  }
}

const nums = [3, 2, 4];
const target = 6;
