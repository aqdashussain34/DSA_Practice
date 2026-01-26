class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        left=0
        max_length=0
        for right in range(len(s)):
            if s[right] in hash_map and hash_map[s[right]] >= left:
                left = hash_map[s[right]] +1
            hash_map[s[right]] =right
            max_length= max(max_length, right-left+1)
        return max_length
        
        