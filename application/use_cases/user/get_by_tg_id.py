from domain.interfaces.InterfaceUserRepository import InterfaceUserRepository
from domain.exceptions.user import UserNotFoundError, NotHavePermissionToGetUser
from domain.entities.user import Role

class GetUserByIdUseCase:
    def __init__(self, repo: InterfaceUserRepository):
        self.repo = repo

    async def execute(self, telegram_id: int, user_tg_id: int):
        admin = await self.repo.get_role(telegram_id)

        if not admin in [Role.admin, Role.moderator]:
            raise NotHavePermissionToGetUser()
        
        user = await self.repo.get_by_tg_id(user_tg_id)
        
        if user is None:
            raise UserNotFoundError(user_tg_id)
        
        return user


        

        
     

        