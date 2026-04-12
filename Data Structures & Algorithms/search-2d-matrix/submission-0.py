class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(self, nums: List[int], target: int) -> bool:
            left = 0
            right = len(nums)-1
            mid = (len(nums))//2

            while left <= right:
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                    mid = (left + right) //2
                else:
                    right = mid-1
                    mid = (left + right)//2
            return False


        for x in matrix:
            if binary_search(self, x,target):
                return True
        return False

        