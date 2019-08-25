# source
# https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d


class Node:
    def __init__(self, data):
        self.data = data
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


class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def add_node(self, node):
        if self.length == 0:
            self.add_beginning(node)
        else:
            self.add_last(node)

    def add_beginning(self, node):
        new_node = node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def add_last(self, node):
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next

        new_node = node
        new_node.next = None
        current_node.next = new_node
        self.length += 1

    def traverse(self):
        node_list = []
        current_node = self.head
        while current_node != None:
            node_list.append(current_node.data)
            current_node = current_node.next

        print(node_list)


node1 = Node(20)
node2 = Node(21)
node3 = Node(22)

linkedlist = LinkedList()
linkedlist.add_node(node1)
linkedlist.add_node(node2)
linkedlist.add_node(node3)
print(linkedlist.traverse())