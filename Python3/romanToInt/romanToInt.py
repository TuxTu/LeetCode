#80ms,14.1MB
class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        ans = 0
        i = 0

        while i < len(s):
            if i < len(s) - 1 and (s[i] + s[i + 1]) in romanDict:
                ans += romanDict[s[i] + s[i + 1]]
                i += 2
            else:
                ans += romanDict[s[i]]
                i += 1

        return ans

print(Solution().romanToInt(input()))