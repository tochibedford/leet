class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x) #push to stack

    def pop(self) -> int:
        stableLength = len(self.stack1)
        while stableLength: 
            lastPopped = self.stack1.pop()
            if stableLength != 1:
                self.stack2.append(lastPopped)
            stableLength -= 1
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())
        return lastPopped
        

    def peek(self) -> int: 
        # len(self.stack1) is basically same as checking if stack1 is empty in this case
        while len(self.stack1): 
            lastPopped = self.stack1.pop()
            self.stack2.append(lastPopped)
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())
        return lastPopped
            

    def empty(self) -> bool:
        if not len(self.stack1):
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()