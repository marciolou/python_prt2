from core.configs import settings
from pydantic import BaseModel

class AlunoModel(settings.DB_BaseModel):
    __tablename__ = 'alunos'

    id: int
    nome: str
    email: str

    class config():
        orm_mode = True
