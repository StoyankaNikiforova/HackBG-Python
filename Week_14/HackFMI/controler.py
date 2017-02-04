import requests
from settings import URL_MENTORS, URL_SKILLS, URL_TEAMS
from model import engine, Team, Skills, Mentor
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()


def get_data(url):
    response = requests.get(url)
    return response.json()


def fill_skill_table():
    all_data = get_data(URL_SKILLS)
    for skill_data in all_data:
        sk_name = skill_data['name']
        skill = Skills(name=sk_name)
        session.add(skill)
        session.commit()

def fill_team_table():
    all_data = get_data(URL_TEAMS)
    for team_data in all_data:
        name = team_data['name']
        idea_description = team_data['idea_description']
        repository = team_data['repository']
        need_more_members = team_data['need_more_members']
        members_needed_desc = team_data['members_needed_desc']
        room = team_data['room']
        place = team_data['place']
        data_row = Mentor(name=name, idea_description=idea_description,
                          repository=repository, need_more_members=need_more_members,
                          members_needed_desc=members_needed_desc, room=room, place=place
                          )
        session.add(data_row)
        session.commit()


def fill_mentors_table():
    all_data = get_data(URL_MENTORS)
    for mentor_data in all_data:
        name = mentor_data['name']
        description = mentor_data['description']
        picture = mentor_data['picture']
        data_row = Mentor(name=name, description=description, picture=picture)
        session.add(data_row)
        session.commit()


def main():
    # fill_skill_table()
    fill_mentors_table()

    fill_team_table()



if __name__ == '__main__':
    main()
