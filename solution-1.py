#using set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        max_length=0
        result=set()
        left=0
        for right in range(n):
            if s[right] not in result:
                result.add(s[right])
                max_length=max(max_length, right-left+1)
            else:
                while s[right] in result:
                    result.remove(s[left])
                    left+=1
                result.add(s[right])
        return max_length
    