class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers)-1
        i=0

        while i<j:
            sum = numbers[i]+numbers[j]
            
            if sum < target:
                i+=1
            elif sum > target:
                j -= 1
            else:
                return [i+1,j+1]
