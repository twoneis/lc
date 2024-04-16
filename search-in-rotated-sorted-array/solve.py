class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        if pivot == -1:
            return self.bin_search(nums, 0, len(nums) - 1, target)
        if target >= nums[0]:
            return self.bin_search(nums, 0, pivot, target)
        return self.bin_search(nums, pivot + 1, len(nums) - 1, target)


    def find_pivot(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        max_pivot = nums[0] - 1
        while l <= r:
            m = (l + r) // 2
            if m + 1 == len(nums):
                return -1
            if nums[m] > nums[m + 1]:
                return m
            elif nums[m] < max_pivot:
                r = m - 1
            else:
                l = m + 1
        return -1
                
    
    def bin_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1
