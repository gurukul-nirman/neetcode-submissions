class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(filter(str.isalnum, s)).lower()
        l = len(new_s)
        i=0
        if(l <= 1):
            return True
        while i<=l//2:
            if new_s[i]!=new_s[-i-1]:
                return False
            i += 1
        
        return True
        