class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights)-1
        i = 0
        ans = -1
        while i<j:
            min_height = min(heights[i], heights[j])
            space = j-i;
            ans = max(ans, min_height*space)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1   
             
        return ans