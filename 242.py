class Solution(object):
    def isAnagram(self, s, t):
        if len(s)==len(t):
            s=list(s)
            s.sort()
            t=list(t)
            t.sort()
            for i in range(len(s)):
                if s[i]!=t[i]:
                    return False
            return True
        return False
                    