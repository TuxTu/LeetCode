#52ms, 13.8MB
class Solution:
    map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def backtrack(self, digitsNum, digits, ans, temp):
        if digitsNum == len(digits):
            ans.append(''.join(temp))
            return
        for ch in self.map[digits[digitsNum]]:
            temp.append(ch)
            self.backtrack(digitsNum + 1, digits, ans, temp)
            temp.pop()

    def letterCombinations(self, digits: str) -> [str]:
        ans = []
        temp = []

        if not digits:
            return []

        self.backtrack(0, digits, ans, temp)
        return ans

print(Solution().letterCombinations('23456789'))