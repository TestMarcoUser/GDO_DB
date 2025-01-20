from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Base per il modello
Base = declarative_base()

# Tabella Prodotto
class Prodotto(Base):
    __tablename__ = 'prodotto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    prezzo = Column(Float, nullable=False)
    categoria = Column(String(50))
    quantità = Column(Integer, nullable=False)
    id_fornitore = Column(Integer, ForeignKey('fornitore.id'))

    fornitore = relationship("Fornitore", back_populates="prodotti")

# Tabella Fornitore
class Fornitore(Base):
    __tablename__ = 'fornitore'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    contatti = Column(String(255))

    prodotti = relationship("Prodotto", back_populates="fornitore")

# Creazione del motore e sessione
DATABASE_URL = "mysql+pymysql://username:password@localhost/GDO_DB"
engine = create_engine(DATABASE_URL, echo=True)

Base.metadata.create_all(engine)  # Crea tutte le tabelle
Session = sessionmaker(bind=engine)
