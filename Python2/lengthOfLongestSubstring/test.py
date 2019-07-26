def lengthOfLongestSubstring(s):
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

print(lengthOfLongestSubstring("pwwekw"))
