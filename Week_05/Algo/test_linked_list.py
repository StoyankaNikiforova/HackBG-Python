import unittest
from linked_list import LinkedList
from linked_list import Node


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_adding_element(self):
        self.ll.add_element(4)
        self.ll.add_element(5)
        self.assertEqual(self.ll.size(), 2)

    def test_remove_element(self):
        self.ll.add_element(4)
        size = self.ll.size()
        self.ll.remove(0)
        size2 = self.ll.size()
        self.assertFalse(size == size2)

    def test_index(self):
        self.ll.add_element(4)
        self.assertEqual(self.ll.index(0).data, 4)

if __name__ == '__main__':
    unittest.main()
