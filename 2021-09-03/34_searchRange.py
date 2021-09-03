class Solution(object):
	#二分查找，主要是边界处理
    def searchLeftIndex(self, nums, target):
        l = 0
        h = len(nums) - 1
        ans = -1
        #查找leftIndex，第一个>= target的位置
        while l <= h:
            mid = (l+h) / 2
            if nums[mid] >= target:
                h = mid - 1
                if nums[mid] == target:
                    ans = mid
            else:
                l = mid + 1
        return ans
    
    def searchRightIndex(self, nums, target):
        l = 0
        h = len(nums) - 1
        ans = -1
        while l <= h:
            mid = (l + h)
            if nums[mid] <= target:
                l = mid + 1
            else:
                h = mid - 1
        if l > len(nums) - 1 or h < 0:
            return -1
        else:
            return l

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftIndex = self.searchLeftIndex(nums, target)
        rightIndex = self.searchRightIndex(nums, target)
        if leftIndex == -1:
            return [-1, -1]
        if leftIndex != -1:
            return [leftIndex, rightIndex]

