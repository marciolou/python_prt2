from typing import Optional
from pydantic import BaseModel

class Funcionarios(BaseModel):
    id: int[Optional] = None
    nome: str
    idade: int
    email: str
