# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars_s, chars_t = {}, {}

        for char_s, char_t in zip(s, t):
            chars_s[char_s] = chars_s.get(char_s, 0) + 1
            chars_t[char_t] = chars_t.get(char_t, 0) + 1

        return chars_s == chars_t
