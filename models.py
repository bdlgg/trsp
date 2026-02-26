from pydantic import BaseModel, field_validator
from typing import Optional

class User(BaseModel):
    name: str
    id: Optional[int] = None
    age: Optional[int] = None

class FeedBack(BaseModel):
    name: str
    message: str
    #для 2.2
    @field_validator('name')
    @classmethod
    def validate_name_len(cls, v):
        if len(v) < 2 or len(v)>50:
            raise ValueError('Name must be between 2 and 50 characters')
        return v

    @field_validator('message')
    @classmethod
    def validate_mes(cls, v):
        if len(v) < 10 or len(v) > 500:
            raise ValueError("Message must be between 10 and 500 characters")
        words = ["кринж", "рофл", "вайб"]  # за что вайб то...
        v_low = v.lower()
        for w in words:
            if w in v_low:
                raise ValueError("Использование недопустимых слов")
        return v

