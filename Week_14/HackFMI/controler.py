import requests
from settings import URL_MENTORS, URL_SKILLS, URL_TEAMS
from model import engine, Team, Skills, Mentor
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()


def get_data(url):
    response = requests.get(url)
    return response.json()


# def fill_row(class_name, **filds):
#     session.add(exec("{}({})".format(class_name, filds)))
#     session.commit()
#     return True

def fill_skill_table():
    all_data = get_data(URL_SKILLS)
    for skill_data in all_data:
        sk_name = skill_data['name']
        skill = Skills(name=sk_name)
        session.add(skill)
        session.commit()


# def fill_team_table():
#     all_data = get_data(URL_TEAMS)
#     for team_data in all_data:
#         name = team_data['name']
#         description = mentor_data['description']
#         picture = mentor_data['picture']
#         data_row = Mentor(name=name, description=description, picture=picture, teams=teams)
#         session.add(data_row)
#         session.commit()


# def fill_mentors_table():
#     all_data = get_data(URL_MENTORS)
#     for mentor_data in all_data:
#         teams = session.query(Team).filter(Team.mentor == mentor_data['id'])
#         name = mentor_data['name']
#         description = mentor_data['description']
#         picture = mentor_data['picture']
#         data_row = Mentor(name=name, description=description, picture=picture, teams=teams)
#         session.add(data_row)
#         session.commit()


def main():
    fill_skill_table()


if __name__ == '__main__':
    main()
