from config.database import Base
from sqlalchemy import Column,  Integer


class Periodo_lectivo(Base):
    __tablename__ = 'PERIODOLECTIVO'

    periodo_id = Column(Integer, primary_key=True)
    anio = Column(Integer)
    bloques = Column(Integer)
    semanas = Column(Integer)