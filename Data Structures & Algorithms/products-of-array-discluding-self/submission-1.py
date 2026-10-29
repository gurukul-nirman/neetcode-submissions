class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        end = [0] * length
        product = 1
        output = [0] * length

        for i in range(length):
            output[i] = product
            product *= nums[i]

        product = 1
        for i in range(length-1, -1, -1):
            end[i] = product
            product *= nums[i]
            output[i] *= end[i]

        return output
        