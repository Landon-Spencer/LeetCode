# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    result = []
    long = l1 if l1 >= l2 else l2
    short = l2 if l2 < l1 else l1
    caryOver = False
    print(f'long {long}, short {short}')
    for num in reversed(long):
      place = long.index(num)
      if num + short[place] > 9:
        result.insert(0, 0)
      else:
        result.insert(0, num + short[place])
    return result


test = Solution()
print(test.addTwoNumbers(l1=[2,4,3], l2=[5,6,4]))
print(test.addTwoNumbers(l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]))
