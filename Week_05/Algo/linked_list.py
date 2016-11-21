class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return "{}".format(self.data)

    def __repr__(self):
        return self.__str__()


class LinkedList:
    def __init__(self):
        self.size_count = 0
        self.head = None

    def add_element(self, data):
        node = Node(data)
        if self.size_count == 0:
            self.head = node
        else:
            curr_node = self.index(self.size_count-1)
            curr_node.next = node
        self.size_count += 1

    def index(self, index):
        node = self.head
        i = 0
        while i < index:
            next_node = node.next
            node = next_node
            i += 1
        return node

    def size(self):
        return self.size_count

    def remove(self, index):
        self.size_count -= 1

    def pprint(self):

        pass

    def to_list(self):
        pass

    def add_at_index(self, index, data):
        pass

    def add_first(self, data):
        pass

    def add_list(self, list1: list):
        pass

    def add_linked_list(self, Linkedlist_my):
        pass

    def ll_from_to(self, start_index, end_index):
        pass

    def pop(self):
        pass

    def reduce_to_unique(self):
        pass
