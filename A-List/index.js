const util = require('util')

class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}

function arrayToList(theArray){
    head = null // --> points to the head of my linked list
    prev = null // --> points to the node I last created while looping
    theArray.forEach((element, index) => {
        nodeElement = new Node(element)
        if(index == 0){
            head = nodeElement
            prev = nodeElement
        }else{
            prev.next = nodeElement
            prev = nodeElement
        }
    });
    return head
}

function listToArray(head){
    theArray = []
    while(head != null){
        theArray.push(head)
        head = head.next
    }
    return theArray
}

function prepend(head, newElement){
    newNode = new Node(newElement)
    newNode.next = head
    return newNode
}

function nth(head, index){
    currIndex = 0
    while(currIndex++<index){
        head = head.next
    }
    if(head == null)
        return undefined
    return head
}

node1 = new Node(1)
node2 = new Node(2)
node3 = new Node(3)

node1.next = node2
node2.next = node3

// nodeNew = new Node(500)

console.log(arrayToList([5,6,7,8,9]))
console.log(listToArray(node1))
console.log(util.inspect(prepend(node1, 500), {showHidden: false, depth: null, colors: true}))


