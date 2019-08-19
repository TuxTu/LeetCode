#180ms
class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        minDiff = 9999
        i = 0
        while i < len(nums):
        	j = i + 1
        	k = len(nums) - 1
        	jCount = 1
        	kCount = 1
        	while j < k:
        		diff = nums[i] + nums[j] + nums[k] - target
        		if diff == 0:
        			return target
        		elif abs(diff) < abs(minDiff):
        			minDiff = diff
        		if jCount == 3:
        			while j + 1 < len(nums) and nums[j] == nums[j + 1]:
        				j += 1
        			jCount = 0
        		if kCount == 3:
        			while k - 1 > 0 and nums[k] == nums[k - 1]:
        				k -= 1
        			kCount = 0
        		if diff < 0:
        			if j + 1 < len(nums) and nums[j + 1] == nums[j]:
	        			jCount += 1
        			j += 1
        		else:
        			if k - 1 > 0 and nums[k] == nums[k - 1]:
        				kCount += 1
        			k -= 1	
        	while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        		i += 1
        	i += 1
        return minDiff + target

print(Solution().threeSumClosest(
	[-1,0,1,1,55], int(input())))
