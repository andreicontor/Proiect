from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float

hostname = "127.0.0.1"
username = "root"
password = ""
port = 33066
database = "clinica"

# engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}', echo=True)
#
# with engine.connect() as connection:
#     print("Connection successful")

Base = declarative_base()
engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}', echo=True)

print(engine.connect())

# class Vanzator(Base):
#     __tablename__ = 'vanzator'
#     id = Column(Integer, primary_key=True)
#     nume = Column(String(30))
#     varsta = Column(Integer)
#     salariu = Column(Integer)
#
#     def __repr__(self):
#         return f"Vanzatorul {self.nume} are {self.varsta} ani si castiga in fiecare luna {self.salariu} lei."
#
# class Produs(Base):
#     __tablename__ = 'produs'
#     id = Column(Integer, primary_key=True)
#     denumire = Column(String(40))
#     pret = Column(Integer)
#
#     def __repr__(self):
#         return f"Produsul {self.denumire} costa {self.pret} lei."

# class Medicament(Base):
#     __tablename__ = 'medicament'
#     id = Column(Integer, primary_key=True)
#     denumire = Column(String(40))
#     data_expirare = Column(Date)
#     pret = Column(Float)
#
#     def __repr__(self):
#         return f"{self.denumire} costa {self.pret} si este valabil pana la {self.data_expirare}"

print(Base.metadata.create_all(engine))



