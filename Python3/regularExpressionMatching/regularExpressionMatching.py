#2384ms,13.8MB
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
    	if not p:
    		return not s
    	
    	firstMatch = bool(s) and (s[0] == p[0] or p[0] == '.')
    	
    	if len(p) >= 2 and p[1] == '*':
    		return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
    	else:
    		return firstMatch and self.isMatch(s[1:], p[1:])

#68ms,13.9MB
class Solution2:
	def isMatch(self, s: str, p:str) -> bool:
		if not p:
			return not s

		dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
		dp[0][0] = True

		for j in range(1, len(p) + 1):
			dp[0][j] = (j >= 2) and p[j - 1] == '*' and dp[0][j - 2]

		for i in range(1, len(s) + 1):
			for j in range(1, len(p) + 1):
				if p[j - 1] == '*':
					dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
				else:
					dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')

		return dp[len(s)][len(p)]


print(Solution2().isMatch(input(), input()))
