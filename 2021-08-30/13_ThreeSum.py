class Solution(object):
	#排序，外层遍历，内层双指针
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums_sorted = sorted(nums)
        i = 0
        for i in range(len(nums)):
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                three_sum = nums_sorted[i] + nums_sorted[j] + nums_sorted[k]
                if three_sum > 0:
                    k = k - 1
                elif three_sum < 0:
                    j = j + 1
                else:
                    res.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                    while k > 0 and nums_sorted[k] == nums_sorted[k-1]:
                        k = k - 1
                    k = k - 1
                    while j < len(nums) - 1 and nums_sorted[j] == nums_sorted[j+1]:
                        j = j + 1
                    j = j + 1
        return res
