class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        dic = {}
        t = 0
        for v in strs:
            x = "".join(sorted(v))
            if x in dic:
                l[dic[x]].append(v)
            else:
                dic[x] = t
                l.append([v])
                t += 1
        
        return l
