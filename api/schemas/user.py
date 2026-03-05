from pydantic import BaseModel, Field
from domain.entities.user import Role, User
from datetime import datetime

class CreateUserDTO(BaseModel):
    username: str = Field(default=None, max_length=32)
    telegram_id: int
    first_name: str | None = Field(..., min_length=1, max_length=100)
    last_name: str | None =  Field(default=None, max_length=100)
    phone_number: str | None =  Field(default=None, max_length=20)

class UserDTO(BaseModel):
    id: int
    username: str | None = None
    role: Role
    first_name: str
    last_name: str | None = None
    telegram_id: int
    phone_number: str | None = None
    created_at: datetime

    @classmethod 
    def from_entity(cls, entity: User):
 
        return cls(
            id=entity.id,
            username = entity.username,
            role = entity.role,
            first_name = entity.first_name,
            last_name = entity.last_name,
            telegram_id = entity.telegram_id,
            phone_number = entity.phone_number,
            created_at = entity.created_at

        )