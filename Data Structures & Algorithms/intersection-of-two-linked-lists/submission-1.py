# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # hash set i shouldve done..
        while(headA):
            point = headB
            while(point):
                if point == headA:
                    return point
                else:
                    point = point.next
            headA = headA.next
        return None
        