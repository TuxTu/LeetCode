#violence
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0		
        for i in range(len(height) - 1):
        	for j in range(i, len(height)):
        		minHeight = min(height[i], height[j])
        		curArea = (j - i) * minHeight
        		if curArea > maxArea:
        			maxArea = curArea
        return maxArea

#double point
class Solution:
    def maxArea(self, height: List[int]) -> int:
    	l, r = 0, len(height) - 1
    	maxArea = 0
    	while l < r:
    		maxArea = max(maxArea, min(height[l], height[r]) * (r - l))
    		if height[l] > height[r]:
    			r -= 1
    		else:
    			l += 1
    	return maxArea
