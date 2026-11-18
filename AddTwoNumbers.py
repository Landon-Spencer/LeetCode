# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    carryOver = False
    result = ListNode()
    head = result
    while l1 is not None and l2 is not None:
      sum = l1.val + l2.val
      if sum + 1 <= 9 and carryOver:
        result.val = sum + 1
        carryOver = False
      elif sum >= 10 and carryOver:
        result.val = sum % 10
      elif sum > 9:
        result.val = sum % 10
        carryOver = True
      else:
        result.val = sum
      l1 = l1.next
      l2 = l2.next
      if l1 is not None or l2 is not None or carryOver:
        result.next = ListNode()
        result = result.next
    while l1 is not None:
      if l1.val == 9 and carryOver:
        result.val = (l1.val + 1) % 10
      elif carryOver:
        result.val = l1.val + 1
        carryOver = False
      else:
        result.val = l1.val
      l1 = l1.next
      if l1 is not None or carryOver:
        result.next = ListNode()
        result = result.next
    while l2 is not None:
      if l2.val == 9 and carryOver:
        result.val = (l2.val + 1) % 10
      elif carryOver:
        result.val = l2.val + 1
        carryOver = False
      else:
        result.val = l2.val
      l2 = l2.next
      if l2 is not None or carryOver:
        result.next = ListNode()
        result = result.next
    if carryOver:
      result.val = 1
    return head

    # result = []
    # long = l1 if l1 >= l2 else l2
    # short = l2 if l2 < l1 else l1
    # carryOver = False
    # print(f'long {long}, short {short}')
    # for i, num in enumerate(long):
    #   if i + 1 > len(short):
    #     for digit in enumerate(long[i:], start=i):
    #       if digit[1] == 9 and carryOver == True and digit[0] == len(long) - 1:
    #         result.append(0)
    #         result.append(1)
    #       elif digit[1] == 9 and carryOver == True:
    #         result.append(0)
    #       elif carryOver == True:
    #         result.append(digit[1] + 1)
    #         carryOver = False
    #       else:
    #         result.append(digit)
    #     break
    #   elif num + short[i] > 9 and carryOver == True:
    #     result.append(((num + short[i]) % 10) + 1)
    #   elif num + short[i] > 9:
    #     carryOver = True
    #     result.append((num + short[i]) % 10)
    #   elif carryOver:
    #     result.append(num + short[i] + 1)
    #     carryOver = False
    #   else:
    #     result.append(num + short[i])
    # return result

test13 = ListNode(3)
test12 = ListNode(4, test13)
test11 = ListNode(2, test12)

test23 = ListNode(4)
test22 = ListNode(6, test23)
test21 = ListNode(5, test22)

test37 = ListNode(9)
test36 = ListNode(9, test37)
test35 = ListNode(9, test36)
test34 = ListNode(9, test35)
test33 = ListNode(9, test34)
test32 = ListNode(9, test33)
test31 = ListNode(9, test32)

test44 = ListNode(9)
test43 = ListNode(9, test44)
test42 = ListNode(9, test43)
test41 = ListNode(9, test42)

test = Solution()
# print(test.addTwoNumbers(l1=[2,4,3], l2=[5,6,4]))
# print(test.addTwoNumbers(l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]))
# print(test.addTwoNumbers(l1=test11, l2=test21))
final = test.addTwoNumbers(l1=test31, l2=test41)
while final is not None:
  print(final.val)
  final = final.next

