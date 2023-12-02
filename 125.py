class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for i in range(len(s)):
            if s[i].isalnum():
                ans=ans+s[i]
        ans=ans.lower()
        for i in range(len(ans)):
            if ans[i]!=ans[-(i+1)]:
                return False
        return True 