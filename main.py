from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import Base, engine
from middlewares.error_handler import errorHandler
from routers.asistencia import asistencia_router

app = FastAPI()
app.title = "Flake Backend"
app.version = "0.0.1"

app.add_middleware(errorHandler)
app.include_router(asistencia_router)

#db
Base.metadata.create_all(bind=engine)

@app.get('/', tags=["Home"])
def read_root():
    return HTMLResponse(content="<h1>Flake-Bcknd</h1>", 
                        status_code=200)