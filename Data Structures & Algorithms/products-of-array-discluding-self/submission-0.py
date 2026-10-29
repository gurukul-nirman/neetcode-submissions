class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        start = [0] * length
        end = [0] * length
        product = 1
        for i in range(length):
            start[i] = product
            product *= nums[i]
        product = 1
        for i in range(length-1, -1, -1):
            end[i] = product
            product *= nums[i]
        output = [0] * length
        for i in range(length):
            output[i] = start[i] * end[i]
        
        return output
        