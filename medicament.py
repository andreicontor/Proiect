from sqlalchemyEx import *
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import func

Session = sessionmaker()
Session.configure(bind = engine)
session = Session()

# date=2020-12-30 time=10-30-30 and timezone=Europe/London
Obj1 = datetime.datetime(year=2020, month=5, day=23)
Obj2 = datetime.datetime(year=2024, month=8, day=20)

paracetamol = Medicament(denumire = "Paracetamol", data_expirare = Obj1, pret = 4.2)
nurofen = Medicament(denumire = "Nurofen", data_expirare = Obj2, pret = 10.3)

# session.add(paracetamol)
# session.add(nurofen)
# session.commit()

medicamente = session.query(Medicament).order_by(Medicament.data_expirare)
for medicament in medicamente:
    print(medicament)

nr_medicamente = session.query(func.count(Medicament.denumire))
print(nr_medicamente)

# In baza de date clinica vrem sa adaugam tabela
# doctor care sa aiba urmatoarele atribute: id, nume, prenume, specializare, varsta

# Ulterior crearii tabelei vrem sa populam cu 5 doctori dupa care sa ii afisam in ordinea varstei, de la cel mai
# in varsta la cel mai tanar


