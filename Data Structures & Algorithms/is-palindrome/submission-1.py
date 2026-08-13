class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid = "qwertyuiopasdfghjklzxcvbnm1234567890"
        n = len(s)
        left = 0
        right = n-1
        while (left <= right):
            if s[left] in valid and s[right] in valid:
                if s[left] != s[right]:
                    return False
                    break
            else:
                if s[left] not in valid:
                    left += 1
                    continue
                else:
                    right -= 1
                    continue
            left+=1
            right-=1
        return True