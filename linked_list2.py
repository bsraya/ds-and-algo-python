# source
# https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def traverse(self):
        node = self
        while node != None:
            print(node.value)
            node = node.next

node1 = Node(12)
node2 = Node(13)
node3 = Node(14)

node1.next = node2
node2.next = node3

print(node1.traverse())