from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from models import User, FeedBack
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
cur_user = User(name="Антон Константинов", id=1)
@app.get("/users")
async def get_user():
    return cur_user

#1.5
@app.post("/user")
async def check_adult(user: User):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

#2.1 и 2.2
feedbacks=[]
@app.post("/feedback")
async def submit_feedback(feedback: FeedBack):
    feedbacks.append(feedback.dict())
    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранен."
    }

