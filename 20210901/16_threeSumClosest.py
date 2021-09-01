class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_sort = sorted(nums)
        i = 0
        min_diff = None
        while i < len(nums_sort) - 1:
            l = i + 1
            h = len(nums_sort) - 1
            while l < h:
                three_sum = nums_sort[i] + nums_sort[l] + nums_sort[h]
                diff = three_sum - target
                if min_diff is None or abs(diff) < min_diff:
                    min_diff = abs(diff)
                    res = three_sum

                if diff < 0:
                    l = l + 1
                else:
                    h = h - 1
            i = i + 1
        return res
