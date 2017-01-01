import getpass
import sqlite3
import sys
from prettytable import PrettyTable
from settings.general_settings import *
from user_interface.user import CinemaUser
from user_interface.reservation import Reservation
from user_interface.validators import *
from settings.messages import *
from queries.manage_db_queris import *


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def welcome():
    user_choice = input(welcome_message)
    switcher = {'1': loggin_user, '2': registration_user, '3': exit}
    return switcher[user_choice]()


def loggin_user():
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    c.execute(GET_PASS_BY_USER, (username,))
    hash_pass = c.fetchone()
    check = verify(password, hash_pass['PASSWORD'])
    if check:
        hello(username)
        chooser(username)
    else:
        print("Wrong passsword")
        exit()


def hello(username):
    print(hello_user.format(username))


def chooser(username):
    print(chooser_message)
    user_choice = input()
    switcher = {'1': show_movies, '2': show_movie_projections,
                '3': make_reservation, '4': cansel_reservation,
                '5': exit, '6': helpp}
    return switcher[user_choice](username)


def registration_user():
    print(registration_message)
    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    if validate_password(password):
        re_password = getpass.getpass('Retype password: ')
        if password == re_password:
            new_user = CinemaUser(username, password)
            new_user.save()
        else:
            print("Password no match")
            exit(username)
    else:
        print('Invalid password')
        exit(username)
    hello(username)
    chooser(username)


def show_movies(username):
    c.execute(GET_MOVIES)
    movies = c.fetchall()
    table = PrettyTable(['Movie ID', 'Name', 'Rating'])
    for m in movies:
        table.add_row([m[0], m[1], m[2]])
    print(table)


def show_movie_projections(username, movie_id):
    c.execute(GET_MOVIES_PROJECTIONS, (movie_id))
    movies = c.fetchall()
    table = PrettyTable(['ID', 'Movie Name', 'Date', 'Time'])
    for m in movies:
        table.add_row([m[0], m[1], m[2], m[3]])
    print(table)


def validate(user_choice, reserv_tickets):
    selected = re.findall('\d+', user_choice)
    row = int(selected[0])
    col = int(selected[1])
    if user_choice in reserv_tickets:
        return resevr_seat_message
    if row > 10 or col > 10:
        return seat_number_out_of_range
    return 'is_valid'


def take_selected_seats(tickets_count, reserv_tickets):
    seats_list = []
    seat_num = 1
    count = int(tickets_count)+1
    while seat_num < count:
        user_choice = input(choose_seat_message.format(seat_num))
        validator = validate(user_choice, reserv_tickets)
        if validator == 'is_valid':
            seat_num += 1
            seats_list.append(user_choice)
        else:
            print(validator)

    return seats_list


def finalize(username, projection_id, seats_list):
    reservations = []
    c.execute(GET_USER_ID_BY_NAME, (username))
    user_id = c.fetchone()
    print(user_id)
    for i in range(len(seats_list)):
        current_seat = seats_list[i]
        current_seat_nums = re.findall('\d+', current_seat)
        row = int(current_seat_nums[0])
        col = int(current_seat_nums[1])

        reservation_row = (user_id, projection_id, row, col)
        reservations.append(reservation_row)

    c.executemany(INSERT_INTO_RESERVATION, reservations)
    db.commit()


def make_reservation(username):
    show_movies(username)
    movie_id = input("Choose movie ID: ")
    show_movie_projections(username, movie_id)
    tickets_count = input('Enter number of tickets: ')
    projection_id = input("Choose projection id: ")

    hall = Reservation.empty_hall()

    c.execute(GET_RESERVED_SPOTS, (projection_id))
    rows_and_cols = c.fetchall()
    reserv_tickets = []
    for value in rows_and_cols:
        row = value[0]
        col = value[1]
        hall[row][col] = 'X'
        reserv_tickets.append(str((row, col)))
    print("The availible seats are '.'")
    for row in hall:
        print(' '.join(row))

    count_reserv = len(rows_and_cols)
    rows_and_cols = c.fetchall()
    print(reserv_tickets)
    seats_list = []
    if (ALL_SPOTS - count_reserv) >= int(tickets_count):
        seats_list = take_selected_seats(tickets_count, reserv_tickets)

    c.execute(GET_PROJECTION_INFO, (projection_id))
    info = c.fetchone()

    finalize = input(final_message.format(info[0], info[1], info[2], ', '.join(seats_list)))
    if finalize = 'finalize':
        print('Thanks')
        finalize(username, projection_id, seats_list)


def cansel_reservation(username):
    pass


def exit(username):
    sys.exit()


def helpp(username):
    pass
