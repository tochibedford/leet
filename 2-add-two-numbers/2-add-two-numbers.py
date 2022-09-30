class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + "->" + str(self.next)
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result: Union[ListNode, None] = None
        head: Union[ListNode, None] = None

        while True:
            addition = l1.val + l2.val + carry
            if addition >= 10:
                carry = 1
                addition = addition - 10
            else:
                carry = 0
            
            if result == None:
                result = ListNode(addition)
                head = result
            else:
                result.next = ListNode(addition)
                result = result.next
            l1 = l1.next
            l2 = l2.next
            if not l1 and not l2:
                if carry:
                    result.next = ListNode(carry)
                break
            if l1 == None:
                while l2:
                    addition =  l2.val + carry
                    if addition >= 10:
                        carry = 1
                        addition = addition - 10
                    else:
                        carry = 0
                    if result == None:
                        result = ListNode(addition)
                        head = result
                    else:
                        result.next = ListNode(addition)
                        result = result.next
                    l2 = l2.next
                if carry:
                    result.next = ListNode(carry)
                break
            elif l2 == None:
                while l1:
                    addition =  l1.val + carry
                    if addition >= 10:
                        carry = 1
                        addition = addition - 10
                    else:
                        carry = 0
                    if result == None:
                        result = ListNode(addition)
                        head = result
                    else:
                        result.next = ListNode(addition)
                        result = result.next
                    l1 = l1.next
                if carry:
                    result.next = ListNode(carry)
                break
        
        return head