## create node structure (nodes contains data,next)

class Node:
    """create a node structure
    """
    def __init__(self,data) -> None:
        self.data=data
        self.next=None #default=None

node1=Node(10) #instance of first node
node2=Node(20) #instance of second node
node3=Node(30)
node4=Node(40)

## assign next address to nodes, connecting nodes to form a linked list
node1.next=node2
node2.next=node4
node4.next=node3

##print
initial=node1
while initial is not None:
    print(initial.data, end="-->")
    initial=initial.next
print("None")
