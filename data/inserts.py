from data.session import Base, Session, connection
from models.Hazard import ChemicalHazards, Replacements

Base.metadata.create_all(connection)
session = Session()