from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.tutor import Tutor
from config.database import Session
from config.database import get_db, Session
from services.tutor import TutorService


tutor_router = APIRouter()

@tutor_router.get('/tutors', tags=["Tutors"])
def get_tutors():
    db = Session()
    tutors = TutorService(db).get_tutors()
    if not tutors:
        return JSONResponse(content={"message": "Tutors not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(tutors), status_code=200)

@tutor_router.get('/tutors/{tutor_id}', tags=["Tutors"])
def get_tutor_by_id(tutor_id: int):
    db = Session()
    tutor = TutorService(db).get_tutor_by_id(tutor_id)
    if tutor is None:
        return JSONResponse(content={"message": "Tutor not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(tutor), status_code=200)

@tutor_router.post('/tutors', tags=["Tutors"])
def create_tutor(tutor: Tutor):
    db = Session()
    query = TutorService(db).add_tutor(tutor)
    return JSONResponse(content={"message": "Tutor created", "tutor": jsonable_encoder(query)}, status_code=201)

@tutor_router.put('/tutors/{tutor_id}', tags=["Tutors"])
def update_tutor(tutor_id: int, tutor: Tutor):
    db = Session()
    query = TutorService(db).update_tutor(tutor_id, tutor)
    if query is None:
        return JSONResponse(content={"message": "Tutor not found"}, status_code=404)
    return JSONResponse(content={"message": "Tutor updated", "tutor": jsonable_encoder(query)}, status_code=200)

@tutor_router.delete('/tutors/{tutor_id}', tags=["Tutors"])
def delete_tutor(tutor_id: int):
    db = Session()
    query = TutorService(db).delete_tutor(tutor_id)
    if query is None:
        return JSONResponse(content={"message": "Tutor not found"}, status_code=404)
    return JSONResponse(content={"message": "Tutor deleted", "tutor": jsonable_encoder(query)}, status_code=200)