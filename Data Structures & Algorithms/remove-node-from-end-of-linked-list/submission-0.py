# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse list, remove then reverse back?
        def reverse(node):
            prev = None
            while(node):
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            return prev

        head = reverse(head)

        #removal
        count = 0
        prev = None
        temp = head
        while(temp):
            count += 1
            if count == n:
                if prev is None:
                    head = temp.next
                else:
                    prev.next = temp.next
                break
            else:
                prev = temp
                temp = temp.next
        
        head = reverse(head)
        return head
        


        