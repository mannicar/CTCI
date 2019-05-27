class Node:

    def __init__(self, val, child = None):
        self.val = val
        self.child = child

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



