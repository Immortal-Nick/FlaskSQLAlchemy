#from faker import Faker
from app import app
from models import db, Presentation

with app.app_context():

    #fake = Faker()

#Deletes the previous data in db first.
    Presentation.query.delete()
#Creting an empty list to append generated data to.
    #presentations = []

    db.session.add(Presentation(name = "Group 10", time = "9:00am"))
    db.session.add(Presentation(name = "Group 10", time = "9:00am"))
    db.session.add(Presentation(name = "Group 10", time = "9:00am"))

    # for n in range (15):
    #     data = Presentation(name = fake.name(), time = fake.time())
    #     presentations.append(data)

    # db.session.add_all(presentations)
    db.session.commit()
    



