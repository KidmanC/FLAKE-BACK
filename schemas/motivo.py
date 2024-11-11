import enum


class Motivo(enum.Enum):
    INASISTENCIA_DEL_DOCENTE = 'Inasistencia del docente'
    FALLA_DE_TRANSPORTE = 'Falla de transporte'
    EMERGENCIA_DE_SALUD = 'Emergencia de salud'
    CONDICIONES_CLIMATICAS = 'Condiciones climáticas'
    AUSENCIA_DE_ESTUDIANTES = 'Ausencia de estudiantes'
    PROBLEMA_TECNICO = 'Problema técnico'
    CIERRE_INSTITUCIONAL = 'Cierre institucional'
    FESTIVO_NO_LABORAL = 'Festivo no laboral'
    OTRO_MOTIVO = 'Otro motivo'