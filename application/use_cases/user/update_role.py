from domain.interfaces.InterfaceUserRepository import InterfaceUserRepository
from domain.exceptions.user import NotHavePermissionToUpdateUser
from domain.entities.user import Role

class UpdateRoleUseCase:
    def __init__(self, repo: InterfaceUserRepository):
        self.repo = repo

    async def execute(self, admin_id: int, telegram_id: int, role: Role):
        admin = await self.repo.get_role(admin_id)

        if not admin in [Role.admin]:
            raise NotHavePermissionToUpdateUser()
         

        return await self.repo.update_role(telegram_id, role)