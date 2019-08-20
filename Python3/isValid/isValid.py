#44ms,13.6MB
class Solution:
	def isValid(self, s: str) -> bool:
		sigStack = []
		sigDict = {'(': ')', '[': ']', '{': '}'}
		for ch in s:
			if ch in sigDict:
				sigStack.append(ch)
			else:
				if not sigStack or sigDict[sigStack.pop()] != ch:
					return False
				else:
					continue

		if not sigStack:
			return True
		else:
			return False

print(Solution().isValid('([{}])'))
