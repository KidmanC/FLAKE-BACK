from config.database import Base
from sqlalchemy import Column,  Integer
from sqlalchemy.orm import relationship


class Periodo_lectivo(Base):
    __tablename__ = 'PERIODOLECTIVO'

    periodo_id = Column(Integer, primary_key=True)
    anio = Column(Integer)
    esta_activo = Column(Integer)

    #back_populates
    #tutores = relationship('Tutor', back_populates='periodo', lazy="joined", join_depth=1)
    #notas = relationship('Nota', back_populates='periodo', lazy="joined", uselist=True, join_depth=1)
    #estudiantes = relationship('Estudiante', back_populates='periodo', lazy="joined", uselist=True, join_depth=1)
    #clases = relationship('Clase', back_populates='periodo', lazy="joined", uselist=True, join_depth=1)
    #aulas = relationship('Aula', back_populates='periodo', lazy="joined", uselist=True, join_depth=1)