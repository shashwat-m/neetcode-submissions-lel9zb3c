class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(s1)-1
        while left <= right:
            if s1[left] != s1[right]:
                return False
            left +=1
            right -=1
        return True