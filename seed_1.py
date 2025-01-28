from sqlalchemy import text
from app import create_app, db
from app.models.person import Person
from dotenv import load_dotenv

load_dotenv()

my_app = create_app()
person1 = Person(name="Gulzhan Jetegenova", dob="1957-08-28", father_id=None, mother_id=None, place_of_birth=None)
person2= Person(name="Nuspali Jetegenov", dob="1957-09-06", father_id=None, mother_id=None, place_of_birth=None)
person3= Person(name="Madina Dzhetegenova", dob="1985-09-05", father_id=person2.id, mother_id=person1.id, place_of_birth=None)
person6= Person(name="Sergey Doroshenko", dob="1983-07-07", father_id=None, mother_id=None, place_of_birth=None)
person4= Person(name="Assel Jetegenova", dob="1983-03-15", father_id=person2.id, mother_id=person1.id, place_of_birth=None)
person10= Person(name="Aitor Arirribas", dob="1980-02-04", father_id=None, mother_id=None, place_of_birth=None)
person9= Person(name="Amaia Arirribas", dob="2015-10-14", father_id=person10.id, mother_id=person4.id, place_of_birth=None) 
person5= Person(name="Keira Doroshenko", dob="2010-09-29", father_id=person3.id, mother_id=person6.id, place_of_birth=None)
person7= Person(name="Alan Doroshenko", dob="2012-11-27", father_id=person3.id, mother_id=person6.id, place_of_birth=None)
person8= Person(name="Marina Doroshenko", dob="2017-11-30", father_id=person3.id, mother_id=person6.id, place_of_birth=None)

with my_app.app_context():
    # Truncate the table and reset IDs
    db.session.execute(text("TRUNCATE TABLE person RESTART IDENTITY CASCADE;"))
    db.session.commit()

    # Add new records
    db.session.add(person1)
    db.session.add(person2)
    db.session.add(person3)
    db.session.add(person4)
    db.session.add(person5)
    db.session.add(person6)
    db.session.add(person7)
    db.session.add(person8)
    db.session.add(person9)
    db.session.add(person10)

    db.session.commit()
