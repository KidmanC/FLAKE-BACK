from models.estudiante import Estudiante as EstudianteModel
from schemas.estudiante import Estudiante

class EstudianteService:
    def __init__(self, db):
        self.db = db

    def get_estudiante(self, filters:dict):
        query = self.db.query(EstudianteModel) 
        for field, value in filters.items():
            if value is not None:  
                query = query.filter(getattr(EstudianteModel, field) == value)
        return query.all()
    
    def get_notas(self, estudiante_id):
        notas = self.db.query(EstudianteModel).filter(EstudianteModel.estudiante_id == estudiante_id).first().notas
        calificaciones = []
        for nota in notas:
            calificaciones.append({"periodo": nota.periodo_id, "nota": nota.calificacion})
        return calificaciones
    
    def add_estudiante(self, estudiante: Estudiante):
        new_estudiante = EstudianteModel(**estudiante.model_dump())
        self.db.add(new_estudiante)
        self.db.commit()
        return new_estudiante

    def update_estudiante(self, estudiante_id, estudiante: Estudiante):
        query = self.db.query(EstudianteModel).filter(EstudianteModel.estudiante_id == estudiante_id).first()
        if not query:
            return None
        query.aula_id = estudiante.aula_id
        query.periodo_id = estudiante.periodo_id
        query.grado_texto = estudiante.grado_texto
        query.grado_num = estudiante.grado_num
        query.identificacion = estudiante.identificacion
        query.tipo_identificacion = estudiante.tipo_identificacion
        query.primer_nombre = estudiante.primer_nombre
        query.segundo_nombre = estudiante.segundo_nombre
        query.primer_apellido = estudiante.primer_apellido
        query.segundo_apellido = estudiante.segundo_apellido
        query.genero = estudiante.genero
        query.fecha_nacimiento = estudiante.fecha_nacimiento
        query.estrato = estudiante.estrato
        self.db.commit()
        return query

    def delete_estudiante(self, estudiante_id):
        estudiante = self.db.query(EstudianteModel).filter(EstudianteModel.estudiante_id == estudiante_id).first()
        if not estudiante:
            return None
        self.db.delete(estudiante)
        self.db.commit()
        return estudiante