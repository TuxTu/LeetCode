from typing import List

#48ms,14MB
class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		res = []
		def backtrack(s = '', left = 0, right = 0):
			if len(s) == 2*n:
				res.append(s)
				return
			if left < n:
				backtrack(s + '(', left + 1, right)
			if right < left:
				backtrack(s + ')', left, right + 1)

		backtrack()
		return res

#64ms,13.7MB
class Solution2:
	def generateParenthesis(self, n: int) -> List[str]:
		if n == 0:
			return ['']
		res = []

		for i in range(n):
			for left in self.generateParenthesis(i):
				for right in self.generateParenthesis(n - 1 - i):
					res.append('{}({})'.format(left, right))

		return res

print(Solution2().generateParenthesis(3))
