class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        s = set(nums)
        strike = 1
        longest = 1
        prev = None
        sorted_set = sorted(s)
        for v in sorted_set:
            if prev != None:
                if v - prev == 1:
                    strike += 1
                    longest = strike if strike > longest else longest
                else:
                    strike = 1
            
            prev = v
        
        return longest
                
