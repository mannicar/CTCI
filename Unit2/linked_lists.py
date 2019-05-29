class Node:

    def __init__(self, val, child = None):
        self.val = val
        self.child = child

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

    def delete(self, node):
        currNode = self.root
        if currNode == node:
            self.root = currNode.child
            return
        while currNode.child is not None:
            if currNode.child == node and currNode.child.child is not None:
                currNode.child = currNode.child.child
                return
            elif currNode.child == node and currNode.child.child is None:
                currNode.child = None
                return
            currNode = currNode.child
        if currNode == node:
            currNode = None

    def __str__(self):
        curr = self.root
        res = "[" + str(curr.val)
        while curr.child is not None:
            res += "," + str(curr.child.val)
            curr = curr.child
        res += "]"
        return res

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
            currNode.delete()

    def buffless_dedupe(self):
        candidateNode = self.root
        pointerNode = self.root.child
        while candidateNode.child is not None:
            while pointerNode is not None:
                if candidateNode.val == pointerNode.val:
                    newNode = pointerNode.child
                    self.delete(pointerNode)
                    pointerNode = candidateNode
                pointerNode = pointerNode.child
            candidateNode = candidateNode.child

    def getNode(self, index):
        currNode = self.root
        if index == 0:
            return currNode
        else:
            return self.getNode(index - 1)

    def revIndex(self, index):
        #get length
        listLen = 1
        currNode = self.root
        while currNode.child is not None:
            listLen += 1
            currNode = currNode.child
        #get forward index
        newIndex = listLen - index
        print ("List is " + str(self))
        print ("List of length: " + str(listLen) + " wants the " + str(index) + "th element from the end, i.e., " + str(newIndex) + "th element.")
        return self.getNode(newIndex)