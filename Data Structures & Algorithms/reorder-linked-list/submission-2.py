# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return 
        #find mid
        slow = head
        fast = head
        prev1 = ListNode(None)

        while(fast and fast.next):
            prev1 = slow
            slow = slow.next
            fast = fast.next.next
        #split off first half
        prev1.next = None

        #reverse second half
        prev = None
        while(slow):
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        #merge two
        final = ListNode(None)
        test = final
        switch = True
        while(head):
            if switch:
                final.next = head
                final = final.next
                head = head.next
                switch = False
            else:
                final.next = prev
                final = final.next
                prev = prev.next
                switch = True
            if head:
                final.next = head
            elif prev:
                final.next = prev





        
        