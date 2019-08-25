class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

    def traverse_from(self):
        node = self
        while node != None:
            print(node.data)
            node = node.next


node1 = Node()
node1.set_data(12)
node2 = Node()
node2.set_data(13)
node3 = Node()
node3.set_data(14)

node1.set_next(node2)
node2.set_next(node3)
print(node1.traverse_from())