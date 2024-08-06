from sqlalchemyEx import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
Session.configure(bind = engine)
session = Session()

vanzator_1 = Vanzator(nume = "Matei", varsta = 32, salariu = 3200)
vanzator_2 = Vanzator(nume = "Luca", varsta = 41, salariu = 3400)

# session.add(vanzator_1)
# session.add(vanzator_2)

vanzator_3 = Vanzator(nume = "Ana", varsta = 23, salariu = 2900)
# session.add(vanzator_3)

vanzatori = session.query(Vanzator).order_by(Vanzator.salariu)

for vanzator in vanzatori:
    print(vanzator)

session.commit()