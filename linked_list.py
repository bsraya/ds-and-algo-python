class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None


# def insert_at_beginning(self, data):
#     newNode = Node()
#     newNode.setData(data)

#     if self.length == 0:
#         self.head = newNode
#     else:
#         newNode.setNext(self.head)
#         self.head = newNode
#     self.length += 1

node1 = Node()
node1.setData(12)
node2 = Node()
node2.setData(13)
node3 = Node()
node3.setData(14)

node1.setNext(node2)
node2.setNext(node3)

print(node1.getNext())
print(node3.getData())