#88ms,16.8MB
class Solution:
	def fourSum(self, nums, target):
		nums.sort()
		result = []
		numsLen = len(nums)
		if numsLen < 4:
			return result
		if nums[0] * 4 > target or nums[numsLen - 1] * 4 < target:
			return result

		numsMap = {}
		for i in range(numsLen):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			for j in range(i + 1, numsLen):
				if j > i + 1 and nums[j] == nums[j - 1]:
					continue
				if nums[i] + nums[j] not in numsMap:
					numsMap[nums[i] + nums[j]] = [[i, j]]
				else:
					numsMap[nums[i] + nums[j]].append([i, j])

		for i in range(numsLen - 1, 2, -1):
			if i < numsLen - 1 and nums[i + 1] == nums[i]:
				continue
			for j in range(i - 1, 1, -1):
				if j < i - 1 and nums[j + 1] == nums[j]:
					continue
				dif = target - nums[i] - nums[j]
				if dif not in numsMap:
					continue
				else:
					for num in numsMap[dif]:
						if num[1] < j:
							result.append([nums[num[0]], nums[num[1]], nums[j], nums[i]])

		return result

from typing import List

#192ms,13.8MB
class Solution2:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		numsLen = len(nums)
		nums.sort()
		result = []

		for i in range(numsLen - 3):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			elif nums[i] + sum(nums[i + 1: i + 3 + 1]) > target:
				break
			elif nums[i] + sum(nums[-1: -3 - 1: -1]) < target:
				continue

			for j in range(i + 1, numsLen -2):
				if j - i > 1 and nums[j] == nums[j - 1]:
					continue
				elif nums[i] + nums[j] + sum(nums[j + 1: j + 2 + 1]) > target:
					break
				elif nums[i] + nums[j] + sum(nums[-1: -2 - 1: -1]) < target:
					continue

				left, right = j + 1, numsLen - 1
				while left < right:
					s = nums[i] + nums[j] + nums[left] + nums[right]
					if s > target:
						right -= 1
						continue
					elif s < target:
						left += 1
						continue
					else:
						result.append([nums[i], nums[j], nums[left], nums[right]])
						while left + 1 < right and nums[left] == nums[left + 1]:
							left += 1
						while right - 1 > left and nums[right - 1] == nums[right]:
							right -= 1
						left += 1
						right -= 1

		return result

print(Solution2().fourSum([1, 0, -1, 0, -2, 2], 0))



