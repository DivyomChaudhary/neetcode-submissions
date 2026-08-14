class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}
        for char in s:
            if char not in mp1:
                mp1[char]=1
            else:
                mp1[char]+=1
        for char in t:
            if char not in mp2:
                mp2[char]=1
            else:
                mp2[char]+=1
        
        if mp1 == mp2:
            return True
        else:
            return False