class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        product = 1
        output = [0] * length

        for i in range(length):
            output[i] = product
            product *= nums[i]

        product = 1
        for i in range(length-1, -1, -1):
            output[i] *= product
            product *= nums[i]

        return output
        