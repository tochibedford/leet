/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    if (head){
        [prevPointer, currPointer] = [head, head.next]
    }else{
        [prevPointer, currPointer] = [head, null]
    }
    while(currPointer){
        if(currPointer.val === prevPointer.val){
            [prevPointer.next, currPointer] = [currPointer.next, currPointer.next]
        }else{
            [prevPointer, currPointer] = [currPointer, currPointer.next]
        }
        
    }
    
    return head
};