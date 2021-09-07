class Solution(object):
	#双指针，较小的数字侧移动
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        i = 0
        j = len(height)-1
        index = 0
        while i < j:
            maxArea = max(min(height[i],height[j])*(j-i), maxArea)
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        return maxArea
