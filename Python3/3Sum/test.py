class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums):
        	j = i + 1
        	k = len(nums) - 1
        	while j < k:
        		sum = nums[i] + nums[j] + nums[k]
        		if sum == 0:
        			ans.append([nums[i], nums[j], nums[k]])
        			j += 1
        			while j < len(nums) and nums[j - 1] == nums[j]:
        				j += 1
        			k -= 1
        			while k > 0 and nums[k + 1] == nums[k]:
        				k -= 1
        		elif sum < 0:
        			j += 1
        			while nums[j - 1] == nums[j]:
        				j += 1
        		elif sum > 0:
        			k -= 1
        			while nums[k + 1] == nums[k]:
        				k -= 1
        	while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        		i += 1
        	i += 1
        return ans

print(Solution().threeSum([0, 0, 0]))
