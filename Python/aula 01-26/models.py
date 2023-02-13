from typing import Optional
from pydantic import BaseModel, validator

class Funcionarios(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    email: str

    @validator('nome')
    def validar_nome(cls, value: str):
        abacate = value.split(' ')
        if len(abacate) < 3:
            raise ValueError('O nome deve ter no minimo 3 espaços')
        return value

funcionarios = [
    Funcionarios(id=1, nome='Marcio', idade=28, email='teste@gmail.com'),
    Funcionarios(id=2, nome='Daniel', idade=24, email='teste@gmail.com')
]
