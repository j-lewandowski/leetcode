# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a

        result = ""
        remainder = 0
        for i in range(len(a) - 1, -1, -1):
            if int(a[i]) + int(b[i]) + remainder > 1:
                result = str((int(a[i]) + int(b[i]) + remainder) % 2) + result
                remainder = 1
            else:
                result = str(int(a[i]) + int(b[i]) + remainder) + result
                remainder = 0
        if remainder == 1:
            result = "1" + result
        return result
