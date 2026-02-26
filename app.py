from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()
#1.1
@app.get("/")
async def root():
    return{"message": "Добро пожаловать в мое приложение FastAPI!"}

#1.2
@app.get("/pages")
async def root():
    return FileResponse("public/index.html")

#1.3
# @app.post("/calculate?num1=5&num2=10")
# async def calculate(num1: int, num2: int):
#     return{"result": 15}

#1.4
