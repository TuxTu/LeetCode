from typing import List

#144ms,15.2MB
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		length = len(nums)
		i = 0
		while i < length:
			if i > 0 and nums[i] == nums[i - 1]:
				del nums[i]
				i -= 1
				length -= 1
			i += 1
		return len(nums)

#112ms,15.4MB
class Solution2:
	def removeDuplicates(self, nums: List[int]) -> int:
		i, j, length = 0, 1, len(nums)
		while j < length:
			if nums[i] != nums[j]:
				i += 1
				nums[i] = nums[j]
			j += 1

		del nums[i + 1: length]

		return i + 1

print(Solution2().removeDuplicates([1, 1, 2]))
