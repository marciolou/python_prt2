from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Path, Query, Header, Depends
from typing import Any, Dict, List
from models import Funcionarios, funcionarios
from time import sleep

app = FastAPI(
    title='MoreDevs2Blu',
    version='007',
    description='FastAPI'
)

def db():
    try:
        print('conexão com banco')
        sleep(1)
    finally:
        print('conexão com banco')
        sleep(1)

@app.get('/', description='Pagina Inicial', summary='Começo de tudo')
async def raiz():
    return {'mensagem': 'Hello World'}

@app.get('/funcionarios')
async def get_funcionarios():
    return funcionarios

@app.get('/funcionarios/{funcio_id}')
async def get_funcionario(funcio_id: int = Path(default=None, title='ID Funcionarios', description='deve ter de 1 à 4', gt=0, lt=4), db: Any = Depends(db)):
    try:
        pessoa = funcionarios[funcio_id]
        return pessoa
    except KeyError:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = 'Funcionario não encontrado'
        )

@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=5), c: int = Query(default=None, gt=5), xdevs: str = Header(default=None)): 
    soma = a + b
    if c:
        soma = soma + c
    print(f'devs: {xdevs}')
    return soma

@app.post('/funcionarios', status_code=status.HTTP_201_CREATED)
async def post_funcionarios(funcio_id: Funcionarios):
    next_id:int = len(funcionarios) +1
    funcio_id.id = next_id
    funcionarios.append(funcio_id)
    return funcio_id

@app.put('/funcionarios/{funcio_id}')
async def put_funcionarios(funcio_id:int, funci: Funcionarios):
    if funcio_id in funcionarios:
        funcionarios[funcio_id] = funci
    else:
        HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Funcionario não encontrado')

@app.delete('/funcionarios/{funcio_id}')
async def delete_funcionarios(funcio_id:int):
    if funcio_id in funcionarios:
        del funcionarios[funcio_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Funcionario não encontrado')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'main.app',
        host = '127.0.0.1',
        port = 8000,
        log_level = 'info',
        reload = True
    )
