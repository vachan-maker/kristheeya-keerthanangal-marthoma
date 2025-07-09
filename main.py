from fastapi import FastAPI,Response
from fastapi.staticfiles import StaticFiles
app = FastAPI()

@app.get("/{songNo}")
async def getSong(songNo:int):
    with open(f'kristheeya_keerthanagal/{songNo}.txt','r',encoding='utf-8') as file:
        text = file.read()
    return Response(content=text,media_type="text/plain; charset=utf-8")