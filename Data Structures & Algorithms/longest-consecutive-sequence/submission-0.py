class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        max_count = 0
        hashMap = {}
        for i in range(n):
            hashMap[nums[i]] = 1
        
        for i in range(n):
            curr_num = nums[i]
            if curr_num - 1 not in hashMap:
                while curr_num + 1 in hashMap:
                    count +=1
                    curr_num +=1
                max_count = max(max_count, count)                 
                count = 1
        return max_count