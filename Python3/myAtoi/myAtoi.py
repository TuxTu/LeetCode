#52ms,13.9MB
class Solution:
    def myAtoi(self, str: str) -> int:
        ans = 0
        length = len(str)
        minus = 1

        i = 0
        while i < length:
            if str[i] != ' ':
                break
            i += 1

        if i < length and str[i] == '+':
            minus = 1
            i += 1
        elif i < length and str[i] == '-':
            minus = -1
            i += 1

        intMax = (1 << 31) - 1
        intMin = 1 << 31
        while i < length and ord(str[i]) >= 48 and ord(str[i]) <= 57:
            ans = ans * 10 + ord(str[i]) - 48
            if minus == -1 and ans > intMin:
                return -intMin
            elif minus == 1 and ans > intMax:
                return intMax
            i += 1

        return ans * minus

#regular expression:
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

print(Solution().myAtoi(input()))
