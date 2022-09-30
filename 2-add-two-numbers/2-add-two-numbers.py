class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + "->" + str(self.next)
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addition = 0
        result: ListNode = ListNode(0)
        head: ListNode = result

        while l1 or l2:
            if l1:
                addition += l1.val
                l1 = l1.next
            if l2:
                addition += l2.val
                l2 = l2.next
            result.next = ListNode(addition % 10)
            result = result.next
            
            addition = 1 if addition > 9 else 0

        if addition:
            result.next = ListNode(addition)
        return head.next