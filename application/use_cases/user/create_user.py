from domain.entities.user import Role
from domain.interfaces.InterfaceUserRepository import InterfaceUserRepository

class CreateUserUseCase:
    def __init__(self, repo: InterfaceUserRepository):
        self.repo = repo

    async def execute(self,
                        username: str | None,
                        first_name: str,
                        last_name: str | None,
                        telegram_id: int,
                        phone_number: str | None 
                    ):
        
        return await self.repo.create (
                telegram_id = telegram_id, 
                username = username,
                first_name = first_name,
                last_name = last_name,
                phone_number = phone_number
            )