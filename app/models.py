from pydantic import BaseModel, EmailStr


class Email(BaseModel):
    to: list[EmailStr]
    subject: str
    message: str
