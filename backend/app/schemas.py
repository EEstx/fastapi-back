from pydantic import BaseModel
from typing import Optional, Dict, List, Any

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class STECreate(BaseModel):
    name: str
    features: Dict[str, Any]

class STEResponse(STECreate):
    id: int
    group_id: Optional[int] = None
    class Config:
        from_attributes = True

class GroupResponse(BaseModel):
    id: int
    name: str
    common_features: Dict[str, Any]
    items: List[STEResponse] = []
    class Config:
        from_attributes = True