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
var reverseList = function(head) {
    let prevPointer = head;
    let currPointer = head ? head.next:null;
    let aheadPointer = (head && head.next) ? head.next.next:null;
    
    if(!prevPointer){
        return null
    }else if(prevPointer && !currPointer){
        return prevPointer
    }
    
    head.next = null
    while(aheadPointer){
        currPointer.next = prevPointer
        prevPointer = currPointer
        currPointer = aheadPointer
        aheadPointer = aheadPointer.next
    }
    currPointer.next = prevPointer
    return currPointer
};