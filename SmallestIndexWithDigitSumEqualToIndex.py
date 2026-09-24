class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index, item in enumerate(nums):
            digits = str(item)
            sum = 0
            for j in digits:
                sum += int(j)
            if sum == index:
                return index
        return -1