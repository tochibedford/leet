/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */

 function ListNode(val) {
    this.val = val;
    this.visited = false
    this.next = null;
}

var hasCycle = function(head) {
    const nodeDict = {};
    let currentNode = head;
    while(currentNode){
        if(currentNode.visited == true){
            return true
        }else{
            currentNode.visited = true
            currentNode = currentNode.next
        }
    }
    return false
        
};