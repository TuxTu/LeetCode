#Manachar,184ms,13.9MB
class Solution:
	def longestPalindrome(self, s: str) -> str:
		newString = "$#"
		for ch in s:
			newString += (ch + "#")
		newString += "@"
		pList = [0] * len(newString)
		id = 1
		maxId = 1
		max = -1
		length = len(newString)
		curMax = -1
		for i in range(length):
			if i >= id + curMax - 1:
				id = i
				curMax = 1
				while i - curMax >= 0 and i + curMax < length and newString[i + curMax] == newString[i - curMax]:
					curMax += 1
				pList[i] = curMax
			else:
				if pList[id + id - i] != id + curMax - i:
					pList[i] = min(pList[id + id - i], id + curMax - i)
				else:
					curMax += id - i
					id = i
					while i - curMax >= 0 and i + curMax < length and newString[i + curMax] == newString[i - curMax]:
						curMax += 1
					pList[i] = curMax


			if pList[i] > max:
				max = pList[i]
				maxId = i

		ans = ""
		iStart = maxId - max + 1
		iEnd = maxId + max - 1
		for i in range(iStart, iEnd):
			if newString[i] != "#":
				ans += newString[i]

		return ans

print(Solution().longestPalindrome(input()))
