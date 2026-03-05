import enum
from datetime import datetime
from dataclasses import dataclass

class Role(str, enum.Enum):
    user = "user"
    moderator = "moderator"
    admin = "admin"

@dataclass
class User:
    id: int
    role: Role
    first_name: str
    telegram_id: int
    created_at: datetime
    
    username: str | None = None
    last_name: str | None = None
    phone_number: str | None = None

    def __post_init__(self):
        if not self.first_name:
            raise ValueError("First name cannot be empty")
        if self.username and len(self.username) > 32:
            raise ValueError("Username too long")
        if not self.telegram_id:
            raise ValueError("Telegram id cannot be empty")
        if not self.role:
            raise ValueError("Role cannot be empty")
        

    def full_name(self) -> str:
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        
        return self.first_name

    def is_admin(self) -> bool:
        return self.role == Role.admin
    
    def is_moderator(self) -> bool:
        return self.role == Role.moderator

    def update_phone(self, phone_number: str):
        if not phone_number or not isinstance(phone_number, str):
            raise ValueError("Phone number is invalid")
        self.phone_number = phone_number

    def update_username(self, username: str | None):
        if username is not None and len(username) > 32:
            raise ValueError("Username too long")
        self.username = username

    # В классе User
    def is_staff(self) -> bool:
        return self.role in [Role.admin, Role.moderator]
    
    