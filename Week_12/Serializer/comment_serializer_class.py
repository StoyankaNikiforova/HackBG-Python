from serializer_class import Serializer
from filds import CharlField, DateTimeField, EmailField


class CommentSerializer(Serializer):
            name = CharlField()
            email = EmailField()
            created_at = DateTimeField()
