from pydantic import BaseModel

class UserSchema(BaseModel):
    email:str
    password:str

class userupdateApikey(BaseModel):
    api_key:str

class userupdateusername(BaseModel):
    username:str