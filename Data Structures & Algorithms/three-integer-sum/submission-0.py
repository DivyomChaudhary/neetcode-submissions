class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        hashMap = {}
        # l, r = 0, 1
        twoSum = 0

        for i in range(n):
            hashMap[nums[i]] = i

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                twoSum = nums[i] + nums[j]
                if -twoSum in hashMap and hashMap[-twoSum] != i  and hashMap[-twoSum] != j:
                    duplicate_checked = sorted([nums[i], nums[j], -twoSum])
                    if duplicate_checked not in res:
                        res.append(duplicate_checked)

        return res