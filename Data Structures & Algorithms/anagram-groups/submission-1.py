class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for v in strs:
            x = "".join(sorted(v))
            if x in dic:
                dic[x].append(v)
            else:
                dic[x] = [v]
        
        return list(dic.values())
