from models import BaseModel
from fields import PKColumn, IntegerColumn, TextColumn


class User(BaseModel):
    __tablename__ = 'user'

    id = PKColumn()
    name = TextColumn(max_length=100)
    age = IntegerColumn(number=20)

    @classmethod
    def create_obj(cls):
        pass


# class Student(User):
#     __tablename__ = 'student'
#     email = TextColumn()
#     shirt_size = IntegerColumn(number=1)
#
#
# # Creating all tables from BaseModel class
# BaseModel.create_all_tables()
#
#
# # Create record in table
# User.create_obj(name="Rosi", age=22)
#
# # Return dict with object
# User.filter(name="Panda")


def main():
    u = User()
    for i in u._registry:
        print(i.__tablename__)


if __name__ == '__main__':
    main()
