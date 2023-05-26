import uuid
import re
from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, validator, constr

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")

class TunedModel(BaseModel):
    class Config:
        orm_mode = True

class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool

class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @validator("name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, datail="name should contains only letters"
            )
        return value

    @validator("surname")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, datail="surname should contains only letters"
            )
        return value

class DeleteUserResponse(BaseModel):
    delete_user_id: uuid.UUID

class UpdateUserResponse(BaseModel):
    updated_user_id: uuid.UUID

class UpdateUserRequest(BaseModel):
    name: Optional[constr(min_lenght=1)]
    surname: Optional[constr(min_lenght=1)]
    email: Optional[EmailStr]

    @validator("name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, datail="name should contains only letters"
            )
        return value

    @validator("surname")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, datail="surname should contains only letters"
            )
        return value