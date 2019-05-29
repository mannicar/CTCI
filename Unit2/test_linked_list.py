from Unit2.linked_lists import Node, LinkedList
import unittest

class TestLinkedLists(unittest.TestCase):
    def test_dedupe(self):
        node1 = Node(5)
        node2 = Node(6, node1)
        node3 = Node(3, node2)
        node4 = Node(2, node3)
        node5 = Node(6, node4)
        ll = LinkedList(node5)

        print ("Original list: "+ str(ll))

        ll.dedupe()

        print ("Deduped list: " + str(ll))

    def test_bufferless_dedupe(self):
        node1 = Node(5)
        node2 = Node(6, node1)
        node3 = Node(3, node2)
        node4 = Node(2, node3)
        node5 = Node(6, node4)
        ll = LinkedList(node5)

        print("Original list: " + str(ll))

        ll.bufferless_dedupe()

        print("Deduped list: " + str(ll))

    def test_pivot(self):

        node1 = Node(5)
        node2 = Node(6, node1)
        node3 = Node(3, node2)
        node4 = Node(2, node3)
        node5 = Node(6, node4)
        node6 = Node(10, node5)
        ll = LinkedList(node6)

        print("Original list: " + str(ll))

        ll.pivot(6)

        print("Pivoted list: " + str(ll))

    def test_int(self):
        node1000 = Node(1)
        node100 = Node(5, node1000)
        node10 = Node(2, node100)
        node1 = Node(3, node10)
        ll = LinkedList(node1)
        integer = int(ll)
        strint = str(ll)
        print(integer)
        print(strint)


