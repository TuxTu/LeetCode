#860ms,12MB
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        length = len(s)
        i = 0
        while i < length:
        	tempS = s[i]
        	j = i + 1
        	while j < length:
        		if s[j] in tempS:
        			break
        		tempS += s[j]
        		j += 1
        	if len(tempS) > sum:
        		sum = len(tempS)
        	i += 1	
        return sum

#56ms,12.6MB
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        maxLength = 0
        slideWindow = ""
        for i in range(length):
        	if s[i] in slideWindow:
        		slideWindow = slideWindow[slideWindow.index(s[i]) + 1:]
        	slideWindow += s[i]
        	if len(slideWindow) > maxLength:
        			maxLength = len(slideWindow)
        return maxLength

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        maxLength = 0
        slideWindow = ""
        for i in range(length):
        	if s[i] in slideWindow:
        		pos = slideWindow.index(s[i])
        		slideWindow = slideWindow[pos + 1:]
        	slideWindow += s[i]
        	if len(slideWindow) > maxLength:
        		maxLength = len(slideWindow)
        return maxLength
