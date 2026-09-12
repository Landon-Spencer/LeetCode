# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        elif not list2:
            return list1
        if len(list2) > len(list1):
            long = list2
            short = list1
        else:
            long = list1
            short= list2
        shortCut = 0
        res = []
        for indexLong, itemLong in enumerate(long):
            for indexShort, itemShort in enumerate(short):
                if itemShort <= itemLong:
                    res.append(itemShort)
                    shortCut += 1
                    if indexShort == len(short) - 1:
                        res.extend(long[indexLong:])
                        return res
                else:
                    res.append(itemLong)
                    del short[:shortCut]
                    shortCut = 0
                    break
        return res

example = Solution()
print(example.mergeTwoLists([1,2,4,5], [1,3,4]))
print(example.mergeTwoLists([1,2,4], [1,3,4,5]))
print(example.mergeTwoLists([1,2,4], [1,3,4]))
print(example.mergeTwoLists([], []))
print(example.mergeTwoLists([], [0]))
print(example.mergeTwoLists([0], []))