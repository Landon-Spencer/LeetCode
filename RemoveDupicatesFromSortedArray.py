class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 1
        for index, val in enumerate(nums):
            if index > 0 and val != nums[index - 1]:
                nums[unique] = val
                unique += 1
        return unique

example = Solution()
input = [1,1,2]
print(example.removeDuplicates(input))
print(input)
print(example.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))