from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return {'mensagem': 'Hello World'}

alunos = {
    1: 'Marcio',
    2: 'Larissa',
    3: 'Marcos',
    4: 'Joao',
}

@app.get('/alunos')
async def get_alunos():
    return alunos

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'main.app',
        host = '127.0.0.1',
        port = 8000,
        log_level = 'info',
        reload = True
    )