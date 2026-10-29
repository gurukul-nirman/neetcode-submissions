class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for v in nums:
            dic[v] += 1;

        l = list(dic.items())
        l.sort(key=lambda x: x[1], reverse=True)
        ans = []
        t=0
        while t<k and t<len(l):
            ans.append(l[t][0])
            t+=1

        return ans