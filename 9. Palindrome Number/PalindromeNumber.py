# leetcode.com/problems/palindrome-number/description/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = x
        reversedNumber = 0
        while tmp > 0:
            reversedNumber = (reversedNumber * 10) + tmp % 10
            tmp //= 10
        return reversedNumber == x
