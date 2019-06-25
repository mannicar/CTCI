# Describe how you could use one array to implement three stacks
from linked_lists import LinkedList, Node
class nStack:

    def __init__(self, n, totalSize):
        
        self.arr = [None for i in range(totalSize)]
        self.stackIndeces = [totalSize/n*i for i in range(n)]

    def nPush(self, n, item):
        if n >= len(self.stackIndeces):
            raise Exception('Stack not defined')
            return
        stackIndex = self.stackIndeces[n]
        while self.arr[stackIndex] is not None:
            stackIndex += 1
            if stackIndex >= len(self.arr) - 1 or (n < len(self.stackIndeces) and stackIndex >= self.stackIndeces[n + 1]):
                raise Exception('Stack ' +str(n)+ ' full')
                return
        self.arr[stackIndex] = item
    
    def nPop(self, n):
        if n >= len(self.stackIndeces):
            raise Exception('Stack ' + str(n) + ' not defined')

        stackIndex = self.stackIndeces[n]
        if (n == len(self.stackIndeces) - 1):
            while (stackIndex + 1 < len(self.arr) - 1) and (self.arr[stackIndex + 1] is not None):
                stackIndex += 1
            res = self.arr[stackIndex]
            self.arr[stackIndex] = None
            return res

        else:
            while (stackIndex + 1 < len(self.arr) - 1) and (stackIndex + 1 < self.stackIndeces[n+1]) and (self.arr[stackIndex + 1] is not None):
                stackIndex += 1
            res = self.arr[stackIndex]
            self.arr[stackIndex] = None
            return res

class Stack:

    def __init__(self):
        self.min = None
        self.stack = Node(None)

    def push(self, item):
        if self.stack.val == None:
            self.stack = Node(item)
            self.min = item
        else:
            lastIn = Node(item, self.stack)
            self.stack = lastIn
            self.min = item if (self.min > item) else self.min

    def pop(self):
        if self.stack is None:
            return None
        val = self.stack.val
        self.stack = self.stack.child
        self.min = None if self.stack is None else self.stack.min_child()
        return val