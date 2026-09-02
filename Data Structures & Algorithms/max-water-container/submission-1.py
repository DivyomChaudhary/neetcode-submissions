class Solution:
    def findArea(left: int, right: int, heights: List[int]) -> int:
        area = (right - left) * min(heights[left], heights[right])
        return area
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        area = 0
        max_area = 0
        while (left < right):
            area = Solution.findArea(left, right, heights)
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return max_area