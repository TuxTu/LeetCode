#92ms,13.9MB
import numpy
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rowsOfOutput = min(len(s), numRows)
        ans = []
        for i in range(rowsOfOutput):
            ans.append("")

        isDownward = 1
        rows = 0
        for ch in s:
            ans[rows] += ch
            rows += isDownward
            if rows == 0 or rows == rowsOfOutput - 1:
                isDownward *= -1

        res = ""
        for string in ans:
            res += string

        return res

#84ms,13.8MB
class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        length = len(s)
        circleLen = 2*numRows - 2
        res = ""

        for i in range(numRows):
            j = 0
            while i + j < length:
                res += s[i + j]
                if j + circleLen - i < length and i != 0 and i != numRows - 1:
                    res += s[j + circleLen - i]
                j += circleLen

        return res

print(Solution2().convert(input(), 3))