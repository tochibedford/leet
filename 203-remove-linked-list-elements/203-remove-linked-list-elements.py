# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        while head and head.val == val:
            head = head.next
         
        prevPointer = head if head else None
        currPointer = head.next if head else None
        while currPointer:
            if currPointer.val == val:
                prevPointer.next = currPointer.next
                currPointer = currPointer.next
            else:
                prevPointer = currPointer
                currPointer = currPointer.next

        return head
            