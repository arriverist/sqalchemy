from flask import Flask
from data import db_session
from data.users import User, Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/1_mars_job.sqlite")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 41
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    db_session.global_init("db/1_mars_job.sqlite")
    user = User()
    user.surname = "Ann"
    user.name = "Ridley"
    user.age = 41
    user.position = "captain's wife"
    user.speciality = "engineer"
    user.address = "module_1"
    user.email = "ann_chief@mars.org"
    user.hashed_password = "wife"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    db_session.global_init("db/1_mars_job.sqlite")
    user = User()
    user.surname = "Mikey"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain' son"
    user.speciality = "sniper"
    user.address = "module_2"
    user.email = "mikey_sniper@mars.org"
    user.hashed_password = "snp"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    db_session.global_init("db/1_mars_job.sqlite")
    user = User()
    user.surname = "Rockie"
    user.name = "Ridley"
    user.age = 91
    user.position = "oldman"
    user.speciality = "constructor"
    user.address = "module_3"
    user.email = "old_man@mars.org"
    user.hashed_password = "old"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    db_session.global_init("db/1_mars_job.sqlite")
    job = Jobs()
    print(db_sess.query(User).first().id)
    job.team_leader = db_sess.query(User).first().id
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()