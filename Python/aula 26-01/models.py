from typing import Optional
from pydantic import BaseModel

class Funcionarios(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    email: str

funcionarios = [
    Funcionarios(id=1, nome='Marcio', idade=28, email='teste@gmail.com'),
    Funcionarios(id=2, nome='Daniel', idade=24, email='teste@gmail.com')
]
