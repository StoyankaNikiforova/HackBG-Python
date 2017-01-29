from model import Client, engine
from validators import validate_pass, encrypt_pass
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()


def edit_message(new_message, logged_user):
    user = get_user(logged_user)
    user.message = new_message
    session.commit()


def edit_pass(new_pass, logged_user):
    user = session.query(Client).filter(Client.username == logged_user).one()
    new_password = set_pass(new_pass)
    user.password = new_password
    session.commit()


@encrypt_pass()
def set_pass(password):
    return password


def register(username, password):
    password = set_pass(password)
    client = Client(username=username, password=password)
    session.add(client)
    session.commit()


def get_user(username):
    user = session.query(Client).filter(Client.username == username).one()
    if user:
        return user
    else:
        return False
