from sqlalchemy import text
from app import create_app, db
from app.models.person import Person
from dotenv import load_dotenv

load_dotenv()

my_app = create_app()

with my_app.app_context():
    # Truncate the table and reset IDs
    db.session.execute(text("TRUNCATE TABLE person RESTART IDENTITY CASCADE;"))
    db.session.commit()

    # Add new records
    db.session.add(Person(name="Gulzhan Jetegenova", dob="1957-08-28", father_id=None, mother_id=None,place_of_birth=None))
    db.session.add(Person(name="Nuspali Jetegenov", dob="1957-09-06", father_id=None, mother_id=None,place_of_birth=None))
    db.session.add(Person(name="Madina Dzhetegenova", dob="1985-09-05", father_id=2, mother_id=2,place_of_birth=None))
    db.session.add(Person(name="Assel Jetegenova", dob="1983-03-15", father_id=2, mother_id=2,place_of_birth=None))
    db.session.add(Person(name="Keira Doroshenko", dob="2010-09-29", father_id=3, mother_id=6,place_of_birth=None))
    db.session.add(Person(name="Sergey Doroshenko", dob="1983-07-07", father_id=None, mother_id=None,place_of_birth=None))
    db.session.add(Person(name="Alan Doroshenko", dob="2012-11-27", father_id=3, mother_id=6,place_of_birth=None))
    db.session.add(Person(name="Marina Doroshenko", dob="2017-11-30", father_id=3, mother_id=6,place_of_birth=None))
    db.session.add(Person(name="Amaia Arirribas", dob="2015-10-14", father_id=10, mother_id=4,place_of_birth=None))
    db.session.add(Person(name="Aitor Arirribas", dob="1980-02-04", father_id=None, mother_id=None,place_of_birth=None))

    db.session.commit()
