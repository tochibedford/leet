class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.left:any = None
        self.right:any = None
        self.parents:list[Node] = [None]*2

    def __str__(self) -> str:
        return str(self.value)

    def __add__(self, otherNode) -> int:
        if otherNode.value:
            return Node(self.value + otherNode.value)
        else:
            return Node(self.value)
    
    def setLeft(self, node):
        self.left = node
        self.left.parents[1] = self
        return self.left

    def setRight(self, node):
        self.right = node
        self.right.parents[0] = self
        return self.right

class PascalTree(object):
    def __init__(self) -> None:
        self.root = Node(1)
    
    def toList(self) -> list[list[int]]:
        treeList:list[list[int]] = []
        treeNodeList:list[list[Node]] = []
        currentNode = self.root
        currentDepth = 0
        while True:
            if len(treeList)-1 >= currentDepth:
                treeList[currentDepth].append(currentNode.value)
                treeNodeList[currentDepth].append(currentNode)
            else:
                treeList.append([currentNode.value])
                treeNodeList.append([currentNode])
            if currentNode.parents[1]:
                currentNode = currentNode.parents[1].right
            elif currentNode.right:
                currentNode = treeNodeList[currentDepth][0].left
                currentDepth += 1
            else:
                break
        return treeList


    def generateNextRow(self) -> None:
        # get to leftmost leaf node
        currentNode = self.root
        while currentNode.left:
            currentNode = currentNode.left
        while True:
            if currentNode.parents[0] and currentNode.parents[1]:     
                left = currentNode.setLeft(currentNode.parents[0].left.right)
                right = currentNode.setRight(currentNode + currentNode.parents[1].right)
            elif currentNode.parents[0]:
                left = currentNode.setLeft(currentNode.parents[0].left.right)
                right = currentNode.setRight(Node(1))
            elif currentNode.parents[1]:
                left = currentNode.setLeft(Node(1))
                right = currentNode.setRight(currentNode + currentNode.parents[1].right)
            else:
                left = currentNode.setLeft(Node(1))
                right = currentNode.setRight(Node(1))
            if currentNode.parents[1]:
                currentNode = currentNode.parents[1].right
            else:
                break

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = PascalTree()
        for i in range(numRows-1):
            pascal.generateNextRow()
        return pascal.toList()
        