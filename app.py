from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
app = FastAPI()
class Calculation(BaseModel):
    num1: int
    num2: int
#1.1
@app.get("/")
async def root():
    return{"message": "Авторелоад реально работает"}

#1.2
@app.get("/pages")
async def root():
    return FileResponse("public/index.html")

#1.3
@app.post("/calculate")
async def calculate(data: Calculation):
    res = data.num1 + data.num2
    return{"result": res}

#1.4
