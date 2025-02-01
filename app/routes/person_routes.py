from flask import Blueprint, abort, make_response, request, Response, jsonify
from app.models.person import Person
from app.db import db
from app.routes.route_utilities import validate_model
from sqlalchemy import text
import os

person_bp = Blueprint("person", __name__, url_prefix="/persons")

@person_bp.get("/ancestor")
def run_sql_file():
    # Path to your SQL file
    sql_file_path = 'family_tree_db_query.sql'

    current_path = os.getcwd()

    if not os.path.exists(sql_file_path):
        return make_response({"error": "SQL file not found" + current_path}, 404)


    # Read the SQL file
    with open(sql_file_path, 'r') as file:
        sql_query = file.read()

    # Execute the SQL query
    result = db.session.execute(text(sql_query))
    db.session.commit()

    # Assuming the query returns rows that can be mapped to the Person model
    persons = result.fetchall()
    # Convert each person to dictionary
    
    results = [row[0] for row in persons]
    response_body = results
    return make_response(response_body, 200)

# @person_bp.get("/search")
# def search_person():
#     name_query = request.args.get("name", "")
#     if not name_query:
#         return make_response([], 200)

#     # Filter by name (assuming partial match). 
#     # Adjust your query logic to suit your needs (case-insensitive, etc.).
#     matching_persons = (
#         db.session.query(Person)
#         .filter(Person.name.ilike(f"%{name_query}%"))
#         .all()
#     )

#     # Convert each person to dictionary
#     results = [person.to_dict() for person in matching_persons]
#     response_body = results
#     return make_response(response_body, 200)

@person_bp.get("")
def get_all_persons():
    query = db.select(Person).order_by(Person.id)
    persons = db.session.scalars(query)

    response_body = [person.to_dict() for person in persons]
    return response_body

@person_bp.get("/<person_id>")
def get_person(person_id):
    person = db.session.get(Person, person_id)
    db.session.add(person)
    db.session.commit()

    return person.to_dict()

@person_bp.post("")
def create_person():
    request_body = request.get_json()
    if "name" not in request_body:
        response_body = {"details": "Invalid data"}
        return make_response(response_body, 400)
    
    name = request_body.get("name")
    dob = request_body.get("dob", None)
    father_id = request_body.get("father_id", None)
    mother_id = request_body.get("mother_id", None)
    place_of_birth = request_body.get("place_of_birth", None)
    
    new_person = Person(name=name, dob=dob, father_id=father_id, mother_id=mother_id, place_of_birth=place_of_birth)
    db.session.add(new_person)
    db.session.commit()

    response_body = new_person.to_dict()
    
    return response_body, 201

@person_bp.delete("/<person_id>")
def delete_person(person_id):
    person = validate_model(Person, person_id)

    db.session.delete(person)
    db.session.commit()

    response_body = {"details": f'Person {person_id},{person.name} successfully deleted.'}
    return make_response(response_body, 200)

@person_bp.put("/<person_id>")
def update_person(person_id):
    person = validate_model(Person, person_id)

    request_body = request.get_json()
    if "name" in request_body:
        person.name = request_body["name"]
    if "dob" in request_body:
        person.dob = request_body["dob"]
    if "father_id" in request_body:
        person.father_id = request_body["father_id"]
    if "mother_id" in request_body:
        person.mother_id = request_body["mother_id"]
    if "place_of_birth" in request_body:
        person.place_of_birth = request_body["place_of_birth"]

    db.session.commit()

    response_body = person.to_dict()
    return response_body, 200