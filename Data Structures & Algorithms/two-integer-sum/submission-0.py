class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        sol = []
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp not in dic:
                dic[nums[i]] = i
            else:
                return [dic[comp], i]
        return sol
