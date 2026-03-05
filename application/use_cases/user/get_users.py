from domain.interfaces.InterfaceUserRepository import InterfaceUserRepository
from domain.exceptions.user import NotHavePermissionToGetUser
from domain.entities.user import Role

class GetUsersUseCase:
    def __init__(self, repo: InterfaceUserRepository):
        self.repo = repo

    async def execute(self, telegram_id: int):
        admin = await self.repo.get_role(telegram_id)

        if not admin in [Role.admin]:
            raise NotHavePermissionToGetUser()
        
        return await self.repo.get_users()