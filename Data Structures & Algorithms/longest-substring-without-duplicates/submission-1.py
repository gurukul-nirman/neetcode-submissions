class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dir = {}
        ans = 0
        start = 0
        end = -1
        for i,v in enumerate(s):
            if v in dir and dir[v] >=start:
                start = dir[v]+1
                end = i
                dir[v] = i
            else:
                end = i
                dir[v]=i
            
            ans = max(ans,end-start+1)
        
        return ans
