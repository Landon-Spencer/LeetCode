class Solution(object):
  def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    return str(x) == str(x)[::-1]

example = Solution()
print(example.isPalindrome(121))
print(example.isPalindrome(-121))
print(example.isPalindrome(12321))
print(example.isPalindrome(123))
