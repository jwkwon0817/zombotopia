from pydantic import BaseModel

class SuccessSchema(BaseModel):
    success: bool = True
    message: str = "Success"

class ErrorSchema(BaseModel):
    success: bool = False
    message: str = "Error"
