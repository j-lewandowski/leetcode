class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and romanNumerals[s[i]] < romanNumerals[s[i + 1]]:
                # substract
                result += romanNumerals[s[i + 1]] - romanNumerals[s[i]]
                i += 1
            else:
                result += romanNumerals[s[i]]
            i += 1
        return result


print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
