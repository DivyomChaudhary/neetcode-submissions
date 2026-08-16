class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        encoded_str = []

        
        for char in strs:
            encoded_str.append(str(len(char)))
            encoded_str.append("#")
            encoded_str.append(char)
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_str = []
        while (i < len(s)):
            j = i
            while s[j] != "#":
                j+=1
            l = int(s[i:j])
            i = j+1
            j = i+l
            decoded_str.append(s[i:j])
            i=j

        return decoded_str