from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import Base, engine
from middlewares.error_handler import errorHandler
from routers.asistencia import asistencia_router
from routers.aula import aula_router
from routers.clase import clase_router
from routers.estudiante import estudiante_router
from routers.clases_no_dadas import clases_no_dadas_router
from routers.horario import horario_router
from routers.institucion import institucion_router
from routers.nota import nota_router
from routers.periodolectivo import periodolectivo_router
from routers.tutor import tutor_router
from routers.auth import auth_router

app = FastAPI()
app.title = "Flake Backend"
app.version = "0.0.1"

app.add_middleware(errorHandler)
app.include_router(asistencia_router)
app.include_router(aula_router)
app.include_router(clase_router)
app.include_router(estudiante_router)
app.include_router(clases_no_dadas_router)
app.include_router(horario_router)
app.include_router(institucion_router)
app.include_router(nota_router)
app.include_router(periodolectivo_router)
app.include_router(tutor_router)
app.include_router(auth_router)


#db
Base.metadata.create_all(bind=engine)

@app.get('/', tags=["Home"])
def read_root():
    return HTMLResponse(content="<h1>Flake-Bcknd</h1>", 
                        status_code=200)