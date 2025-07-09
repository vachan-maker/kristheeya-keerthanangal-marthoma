from fastapi import FastAPI,Response,HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import json
app = FastAPI()



@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

@app.get("/{songNo}")
async def getSong(songNo:int):
    try:
        with open(f'kristheeya_keerthanagal/{songNo}.txt','r',encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Song not found")
    except Exception as e:
        raise HTTPException(status_code=500,detail="Internal Server Error")

    return {"songNo":songNo,"lyrics":text}