from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        l = len(s)
        counts = Counter(nums)
        ans = set()
        for i,x in enumerate(s):
            for j in range(i+1, l, 1):
                rem = x+s[j];
                c = counts[-rem]

                s_temp = sorted([x, s[j], -rem])
                if c > 0:
                    if (x == -rem and s[j] == -rem) and c>=3:
                        ans.add(tuple(s_temp))
                    elif (x == -rem or s[j] == -rem) and c>=2 and x!=s[j]:
                        ans.add(tuple(s_temp))
                    elif (x != -rem and s[j] != -rem):
                        ans.add(tuple(s_temp))

        return [list(i) for i in ans]
