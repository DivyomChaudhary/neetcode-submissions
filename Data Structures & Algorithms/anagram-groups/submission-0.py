class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        index_anag = {}
        res = [[] for i in range(n)]
        for i in range(n):
            char = list(strs[i])
            char.sort()
            key = "".join(char)

            if key not in index_anag:
                index_anag[key] = []

            index_anag[key].append(strs[i])
        return (list(index_anag.values()))