import unittest
from stacks_and_heaps import nStack, Stack
from linked_lists import LinkedList, Node

class TestStacksAndHeaps(unittest.TestCase):

    def test_nStack(self):
        testNStack = nStack(3, 60)
        self.assertTrue(isinstance(testNStack, nStack))
        self.assertTrue(testNStack.stackIndeces[0] == 0)
        self.assertTrue(testNStack.stackIndeces[1] == 20)
        self.assertTrue(testNStack.stackIndeces[2] == 40)
        self.assertTrue(len(testNStack.stackIndeces) == 3)

    def test_nStack_nPush(self):
        testNStack = nStack(3, 10)
        with self.assertRaises(Exception) as context:
            testNStack.nPush(3,1)
        testNStack.nPush(0, 3)
        self.assertTrue(testNStack.arr == [3, None, None, None, None, None, None, None, None, None])
        testNStack.nPush(2, 5)
        self.assertTrue(testNStack.arr == [3, None, None, None, None, None, 5, None, None, None])
        with self.assertRaises(Exception) as context:
            testNStack.nPush(0,6)
            testNStack.nPush(0,7)
            testNStack.nPush(0,8)
        
    def test_nStack_nPop(self):
        testNStack = nStack(4,16)
        with self.assertRaises(Exception) as context:
            testNStack.nPop(4)
        
        testNStack.nPush(2, 3)
        self.assertTrue(testNStack.nPop(2) == 3)
        self.assertTrue(testNStack.arr == [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])

        testNStack.nPush(3, 3)
        self.assertTrue(testNStack.nPop(3) == 3)
        self.assertTrue(testNStack.arr == [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])

        testNStack.nPush(2, 3)
        testNStack.nPush(2, 4)
        testNStack.nPush(2, 5)
        self.assertTrue(testNStack.nPop(2) == 5)
        self.assertTrue(testNStack.nPop(2) == 4)
        self.assertTrue(testNStack.nPop(2) == 3)

    def test_stack(self):
        testStack = Stack()
        self.assertTrue(isinstance(testStack, Stack))

    def test_stack_push(self):
        testStack = Stack()
        testStack.push(1)
        testStack.push(2)
        testStack.push(3)
        self.assertTrue(isinstance(testStack.stack, Node))
        self.assertTrue(testStack.stack.val == 3)
        self.assertTrue(testStack.stack.child.val == 2)
        self.assertTrue(testStack.stack.child.child.val == 1)

    def test_stack_pop(self):
        testStack = Stack()
        testStack.push(1)
        testStack.push(2)
        testStack.push(3)
        val1 = testStack.pop()
        val2 = testStack.pop()
        val3 = testStack.pop()
        self.assertTrue(val1 == 3)
        self.assertTrue(val2 == 2)
        self.assertTrue(val3 == 1)
        valNone = testStack.pop()
        self.assertTrue(valNone is None)

    def test_stack_min(self):
        testStack = Stack()
        testStack.push(5)
        self.assertTrue(testStack.min == 5)
        testStack.push(2)
        self.assertTrue(testStack.min == 2)
        testStack.push(3)
        self.assertTrue(testStack.min == 2)
        testStack.pop()
        self.assertTrue(testStack.min == 2)
        testStack.pop()
        self.assertTrue(testStack.min == 5)
        testStack.pop()
        self.assertTrue(testStack.min is None)

       



if __name__ == '__main__':
    unittest.main()