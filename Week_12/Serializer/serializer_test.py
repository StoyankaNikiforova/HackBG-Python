import unittest
from serializer_class import Serializer
from comment_class import Comment
from comment_serializer_class import CommentSerializer


class TestSerializer(unittest.TestCase):
    def setUp(self):
        self.comment = Comment(email='radorado@hakbulgaria.com', content='wie naistina li hakvate?')
        self.serializer = CommentSerializer(self.comment)

    def test_is_valid(self):
        self.assertTrue(self.serializer.is_valid())

    def test_get_data(self):
        self.assertEqual(self.serializer.data, {' ': 'hsk'})

if __name__ == '__main__':
    unittest.main()
