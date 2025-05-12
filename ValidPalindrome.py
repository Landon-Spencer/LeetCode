class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    filtered_string = ''.join(e for e in s if e.isalnum())
    lower_filtered_string = filtered_string.lower()
    return lower_filtered_string == lower_filtered_string[::-1]


example = Solution()
print(example.isPalindrome("A man, a plan, a canal: Panama"))
print(example.isPalindrome("race a car"))
print(example.isPalindrome(" "))
