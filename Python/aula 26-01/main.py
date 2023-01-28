from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Funcionarios

app = FastAPI()

@app.get('/')
async def raiz():
    return {'mensagem': 'Hello World'}

funcionarios = {
    1:{'nome': 'Marcio', 'idade':28, 'email':'teste@gmail.com'},
    2:{'nome': 'Daniel', 'idade':28, 'email':'teste@gmail.com'},
    3:{'nome': 'Fabio', 'idade':28, 'email':'teste@gmail.com'},
    4:{'nome': 'Robin', 'idade':28, 'email':'teste@gmail.com'},
}

@app.get('/funcionarios')
async def get_funcionarios():
    return funcionarios

@app.get('/funcionarios/{funcio_id}')
async def get_funcionario(funcio_id: int):
    try:
        pessoa = funcionarios[funcio_id]
        funcionarios.update({'id':funcio_id})
        return pessoa
    except KeyError:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = 'Funcionario não encontrado'
        )

@app.post('/funcionarios')
async def post_funcionarios(funcio_id: Funcionarios):
    next_id = len(funcionarios)
    funcionarios[next_id] = funcio_id
    return funcio_id

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'main.app',
        host = '127.0.0.1',
        port = 8000,
        log_level = 'info',
        reload = True
    )
