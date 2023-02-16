from typing import Optional
from sqlmodel import Field, SQLModel 

class ProfModel(SQLModel, table=True):
    __tablename__: str = 'professor'

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str
