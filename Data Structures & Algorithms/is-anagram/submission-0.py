class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            dic[i] = dic[i]+1 if (i in dic) else 1

        for i in t:
            if i in dic:
                dic[i] = dic[i]-1
                if dic[i] == 0:
                    del dic[i]
            else:
                return False

        return True if len(dic) == 0 else False
