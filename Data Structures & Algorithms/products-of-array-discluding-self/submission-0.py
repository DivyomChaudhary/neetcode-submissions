class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = [1]*n
        suf_prod = [1]*n
        res = []
        for i in range(1,n):
            pre_prod[i] = nums[i-1] * pre_prod[i-1]
        for i in range(n-2,-1,-1):
            suf_prod[i] = nums[i+1] * suf_prod[i+1]
            
        for i in range(n):
            res.append(pre_prod[i] * suf_prod[i])
        return res