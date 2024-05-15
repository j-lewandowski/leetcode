# https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:
        closingParenth = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in closingParenth:
                if len(stack) > 0:
                    if stack[-1] == closingParenth[char]:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
