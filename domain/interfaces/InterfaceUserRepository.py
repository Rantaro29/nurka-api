from abc import ABC, abstractmethod
from typing import List
from domain.entities.user import User
from domain.entities.user import Role

class InterfaceUserRepository(ABC):  

    @abstractmethod
    async def get_by_tg_id(self, telegram_id: int) -> User:
      
        pass

    @abstractmethod
    async def create(self, telegram_id: int, username: str, first_name: str,
                    last_name: str | None, phone_number: str | None , role: Role = Role.user) -> User:

        pass

    @abstractmethod
    async def get_role(self, telegram_id: int) -> Role:

        pass

    @abstractmethod
    async def update_role(self, telegram_id: int, new_role: Role) -> User:
    
        pass

    @abstractmethod
    async def get_users(self) -> List[User]:

        pass
