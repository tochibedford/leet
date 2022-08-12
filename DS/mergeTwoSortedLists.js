/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
 var mergeTwoLists = function(list1, list2) {
    let dListHead = new ListNode()
    let dListPointer = dListHead
    while(list1 && list2){
        if (list1.val <= list2.val){
            dListPointer.next = list1
            dListPointer = dListPointer.next
            list1 = list1.next
            dListPointer.next = null
        }else{
            dListPointer.next = list2
            dListPointer = dListPointer.next
            list2 = list2.next
            dListPointer.next = null
        }
    }
    
    if(list1){
        dListPointer.next = list1
    }else if(list2){
        dListPointer.next = list2
    }
    dListHead = dListHead.next
    return dListHead
};
