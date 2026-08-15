class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq_map = {}
        bucket = [[] for i in range(len(nums)+1)]
        res = []
        cnt = 0
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        for key,value in freq_map.items():
            bucket[value].append(key)
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                for num in bucket[i]:
                    if (cnt < k):
                        res.append(num)
                        cnt +=1
        return res