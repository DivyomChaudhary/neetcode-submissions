class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        range_sum = (n*(n+1))//2
        current_sum = sum(nums)
        return range_sum - current_sum