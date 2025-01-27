from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

class Person(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    dob: Mapped[Optional[str]]
    father_id: Mapped[Optional[int]] = mapped_column(ForeignKey("person.id"))
    mother_id: Mapped[Optional[int]] = mapped_column(ForeignKey("person.id"))
    place_of_birth: Mapped[Optional[str]]

# This is a method that returns a dictionary representation of the Person instance
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "dob": self.dob,
            "father_id": self.father_id,
            "mother_id": self.mother_id,
            "place_of_birth": self.place_of_birth
        }
# This is a class method that creates a new Person instance from a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            dob=data["dob"],
            father_id=data.get("father_id"),
            mother_id=data.get("mother_id")
        )

