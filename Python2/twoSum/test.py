def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
        	j = i + 1
        	while j < len(nums):
        		if nums[i] + nums[j] == target:
        			return [i, j]
        		j += 1
        	i += 1
        return []

print(twoSum([1,2,3], 5))
