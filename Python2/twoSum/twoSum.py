#5168ms, 12.7MB
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        size = len(sums)
        while i < size:
        	j = i + 1
        	while j < size:
        		if nums[i] + nums[j] == target:
        			return [i, j]
        		j += 1
        	i += 1
        return []

#48模ms, 13.4MB
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _dict = {}
        for i, m in enumerate(nums):
        	_dict[m] = i
        	
        for i, m in enumerate(nums):
        	j = _dict.get(target - m)
        	if j is not None and i != j:
        		return [i, j]
        return[]
