from fastapi import APIRouter

from Api.v1.endpoints import aluno
from Api.v1.endpoints import usuario

api_router = APIRouter()

#/api/v1/alunos
api_router.include_router(aluno.router, prefix='/alunos', tags=["alunos"])
api_router.include_router(usuario.router, prefix='/usuarios', tags=["usuarios"])
