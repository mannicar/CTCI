class Node:

    def __init__(self, val, child = None):
        self.val = val
        self.child = child

    def __str__(self):
        res = ""
        currNode = self
        while currNode is not None:
            res += str(currNode.val) + "->"
            currNode = currNode.child
        return res

    # 2.3
    def delete(self):
        if self.child is not None:
            self.val = self.child.val
            if self.child.child is not None:
                self.child = self.child.child
            else:
                self.child = None
        else:
            self = None

class LinkedList:

    def __init__(self, root):
        self.root = root

    def getNode(self, index):
        currNode = self.root
        if index == 0:
            return currNode
        else:
            return self.getNode(index - 1)

    def get_length(self):
        res = 0
        currNode = self.root
        while currNode is not None:
            res += 1
            currNode = currNode.child
        return res

    def add(self, other):
        if self.root is None and other.root is None:
            return
        elif self.root is None:
            self.root = other.root
            return
        elif other.root is None:
            return
        else:
            currNode = self.root
            while currNode.child is not None:
                currNode = currNode.child
            currNode.child = other.root

    def append(self, val):
        if self.root is None:
            self.root = Node(val, None)
        else:
            currNode = self.root
            while currNode.child is not None:
                currNode = currNode.child
            currNode.child = Node(val, None)

    def prepend(self, val):
        if self.root is None:
            self.root = Node(val, None)
        else:
            self.root = Node(val, self.root)

    def delete(self, node):
        if self.root == node:
            self.root = self.root.child
        else:
            node.delete()

    def reverse(self):
        if self.root is None:
            return
        else:
            res = LinkedList(Node(self.root.val, None))
            currNode = self.root
            while currNode.child is not None:
                currNode = currNode.child
                res.prepend(currNode.val)
            self.root = res.root


    def __str__(self):
        curr = self.root
        res = "[" + str(curr.val)
        while curr.child is not None:
            res += "," + str(curr.child.val)
            curr = curr.child
        res += "]"
        return res

    # 2.1a
    def dedupe(self):
        buff = {}
        currNode = self.root
        while currNode.child is not None:
            if currNode.val not in buff.keys():
                buff[currNode.val] = 1
            else:
                self.delete(currNode)
            currNode = currNode.child
        if currNode.val in buff.keys():
            self.delete(currNode)

    # 2.1b
    def buffless_dedupe(self):
        candidateNode = self.root
        pointerNode = self.root.child
        while candidateNode.child is not None:
            while pointerNode is not None:
                if candidateNode.val == pointerNode.val:
                    self.delete(pointerNode)
                    pointerNode = candidateNode
                pointerNode = pointerNode.child
            candidateNode = candidateNode.child


    # 2.2
    def revIndex(self, index):
        listLen = 1
        currNode = self.root
        while currNode.child is not None:
            listLen += 1
            currNode = currNode.child
        newIndex = listLen - index
        return self.getNode(newIndex)

    # 2.4
    def pivot(self, val):
        currNode = self.root
        lessList = LinkedList(None)
        moreList = LinkedList(None)
        while currNode.child is not None:
            if currNode.val < val:
                lessList.append(currNode.val)
            else:
                moreList.append(currNode.val)
            currNode = currNode.child
        if currNode.val < val:
            lessList.append(currNode.val)
        else:
            moreList.append(currNode.val)
        lessList.add(moreList)
        self.root = lessList.root

    # 2.5
    def __int__(self):
        res = 0
        if self.root is None:
            return 0
        currNode = self.root
        factor = 1
        while currNode is not None:
            res += currNode.val * factor
            currNode = currNode.child
            factor *= 10
        return res

    def sum_list(self, other):
        return self.int() + other.int()

    # 2.6
    def is_palindrome(self):
        l = self.get_length()
        currList = LinkedList(self.root)
        revList = self.reverse()
        for i in range(l):
            if currList.getNode(i).val != revList.getNode(i).val:
                return False
        return True



