class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return "{}".format(self.data, self.next)

    def __repr__(self):
        return self.__str__()


class LinkedList:
    def __init__(self):
        self.size_count = 0
        self.head = None
        self.tail = None

    def add_element(self, data):
        new_node = Node(data)
        if self.size_count == 0:
            self.head = new_node
        else:
            if self.size_count == 1:
                self.head.next = new_node
            else:
                self.tail.next = new_node
            self.tail = new_node
        self.size_count += 1
        return True

    def __str__(self):
        return self.pprint()

    def __repr__(self):
        return self.__str__()

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
        self.index(index-1).next = self.index(index + 1)
        s = index
        for i in range(s, self.size_count-2):
            self.index(i).data = self.index(i+1).data
            self.index(i).next = self.index(i+1).next

        self.size_count -= 1

    def pprint(self):
        liked_l = self.to_list()
        return ",".join(map(str, liked_l))

    def to_list(self):
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next
        return result

    def add_at_index(self, index, data):
        new_node = Node(data)
        self.index(index-1).next = new_node
        self.index(index).next = self.index(index + 1)
        new_node.next = self.index(index)
        self.size_count += 1

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        node_head = self.head
        self.head = new_node
        self.head.next = node_head

    def add_list(self, items_in_list):
        for item in items_in_list:
            self.add_element(item)

    def add_linked_list(self, ll):
        ll_list = ll.to_list()
        self.add_list(ll_list)

    def ll_from_to(self, start_index, end_index):
        new_ll = LinkedList()
        self_list = self.to_list()
        s = start_index
        e = end_index
        new_ll_list = [self_list[x] for x in range(s, e+1)]
        new_ll.add_list(new_ll_list)
        return new_ll

    # def pop(self):
    #     pass
    #
    def reduce_to_unique(self):
        dict_el = {}
        for i in range(self.size()):
            value = self.index(i)
            dict_el[value.data] = 1
        l = LinkedList()
        l.add_list(list(dict_el.keys()))
        return l

def main():
    l = LinkedList()
    l.add_element(2)
    l.add_element(5)
    l.add_element(6)
    l.add_element(3)
    l.add_first(8)
    l.remove(3)
    l.add_list([11, 45, 69, 3])
    l2 =LinkedList()
    l2.add_element(2)
    l2.add_element(5)
    l2.add_element(6)
    l2.add_element(3)
    l.add_linked_list(l2)
    l3 = LinkedList()
    l3.add_list([4, 8, 4])
    print(l3)
    print(l.ll_from_to(3, 6))

    print(l.reduce_to_unique())
    print(l.index(3))
    # print(l.index(4))
    print(l.tail)
    print(l.pprint())

if __name__ == '__main__':
    main()
