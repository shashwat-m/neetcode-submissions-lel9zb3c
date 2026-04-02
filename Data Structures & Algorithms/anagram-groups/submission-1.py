class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [[strs[0]]]
        dic = {}
        for i in range(len(strs)):
            if tuple(sorted(strs[i])) not in dic:
                dic[tuple(sorted(strs[i]))] = [strs[i]]
            else:
                dic[tuple(sorted(strs[i]))].append(strs[i])
        
        for key in dic:
            sol.append(dic[key])
        return sol


