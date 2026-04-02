class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        dic1 = {}
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] =1
            else:
                dic1[s[i]] += 1
        
        dic2 = {}
        for i in range(len(t)):
            if t[i] not in dic2:
                dic2[t[i]] =1
            else:
                dic2[t[i]] += 1

        return (dic2 == dic1)
        """
        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):

            if s != t:
                return False

        return True
        