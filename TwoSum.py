class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for firstNum in range(len(nums)):
            for secondNum in range(firstNum + 1, len(nums)):
                if (nums[firstNum] + nums[secondNum] == target):
                    return [firstNum, secondNum]

example = Solution()
print(example.twoSum(nums=[2,7,11,15], target=9))
print(example.twoSum(nums=[3,2,4], target=6))
print(example.twoSum(nums=[3,3], target=6))