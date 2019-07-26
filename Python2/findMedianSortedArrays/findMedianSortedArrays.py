class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        allNums = nums1 + nums2
        allNums.sort()
        length = len(allNums)
        isOdd = (length % 2 != 0)
        i = 0
        if isOdd:
        	mid = (length + 1) / 2
        	while i != mid - 1:
        		i += 1
        	return allNums[i]
        else:
        	mid = length / 2
        	while i != mid - 1:
        		allNums.pop()
        		i += 1
        	return (allNums[i] + allNums[i + 1] / 2
