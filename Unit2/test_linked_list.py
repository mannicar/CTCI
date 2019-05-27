from Unit2.linked_lists import Node, LinkedList

node1 = Node(5)
node2 = Node(6, node1)
node3 = Node(3, node2)
node4 = Node(2, node3)
node5 = Node(6, node4)
ll = LinkedList(node5)

print ("Original list: "+ str(ll))

ll.dedupe()

print ("Deduped list: " + str(ll))