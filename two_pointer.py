class TwoSum:
    def solution(self, nums, target):
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > target:
                r = r - 1
            elif nums[l] + nums[r] < target:
                l = l + 1
            else:
                return True
        return False