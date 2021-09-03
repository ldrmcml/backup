class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = (h + l) / 2
            #l,mid升序
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            #mid,h升序
            else:
                if nums[mid] <= target < nums[0]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1
