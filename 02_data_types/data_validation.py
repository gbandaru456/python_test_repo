from datetime import datetime
from typing import Self,Literal
from pydantic import BaseModel,PositiveInt,ValidationError,model_validator

class User(BaseModel):
    id: int
    name: str
    sign_up: datetime | None
    tastes: dict[str,PositiveInt]
    password: str
    @model_validator(mode='after')
    def password_check(self) -> Self:
         if self.password != '2535' :
              raise ValueError("password not match")
         return self
         


external_date = {
    'id':12,
    'name':'Kumar',
    'sign_up':'2019-06-01 12:22',
    'tastes':{
        'wine':9,
        'cheese':10,
        'cabbage':'1'
    },
    'password':'12345'
}
try:
        User(**external_date)
except ValidationError as e:
    print(e.errors())
