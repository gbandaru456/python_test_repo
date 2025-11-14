from pydantic import BaseModel, Field,field_validator
import uuid
from datetime import date,datetime,timedelta
from typing import Union,Literal
from enums import DepartmentEnum 

class Module(BaseModel):
    id: Union[int,uuid.UUID] = Field(exclude=True)
    name: str
    professor: str
    credits: Literal[10,20] = Field(...,description='must be between two values')
    registration_code: str =Field(default='abc')


class Student(BaseModel):
    id: uuid.UUID = Field(exclude=True)
    name: str
    date_of_birth:date =Field(...,description='date of birth values',default_factory=lambda:datetime.today().date())
    GPA: float=Field(...,ge=0,le=4,description='Decimal filed')
    course:Union[str,None]
    department:DepartmentEnum
    fees_paid:bool
    modules: list[Module] = Field(default=[],max_length=3)
    @field_validator('date_of_birth')
    @classmethod
    def birth_16_over_ensure(cls,value:date) -> date:
        sixteen_yeras_ago = datetime.now() - timedelta(days=365*16)
        sixteen_yeras_ago = sixteen_yeras_ago.date()
        if value > sixteen_yeras_ago :
            raise ValueError("Too young to enroll, Sorry!")
        return value
    # @field_validator('modules')
    # @classmethod
    # def module_ensure(cls,value:list) -> list:
    #     for values in value:
    #         print(values)
        
      
      
           
            

  