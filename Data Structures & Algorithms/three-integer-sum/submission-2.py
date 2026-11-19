from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        l = len(s)
        counts = Counter(nums)
        ans = []
        dic = {}
        for i,x in enumerate(s):
            for j in range(i+1, l, 1):
                rem = x+s[j];
                c = counts[-rem]

                s_temp = sorted([x, s[j], -rem])
                sum = x + s[j]
                se = frozenset(set(s_temp))
                if c > 0:
                    if se in dic:
                        continue
                    if (x == -rem and s[j] == -rem) and c>=3:
                        dic[se] = 1
                        ans.append(s_temp)
                    elif (x == -rem or s[j] == -rem) and c>=2 and x!=s[j]:
                        dic[se] = 1
                        ans.append(s_temp)
                    elif (x != -rem and s[j] != -rem):
                        dic[se] = 1
                        ans.append(s_temp)

        return ans
