from domain.exceptions.channel import NotHavePermissionToAddChannel
from domain.exceptions.user import UserNotFoundError
from domain.interfaces.InterfaceChannelRepository import InterfaceChannelRepository
from domain.interfaces.InterfaceUserRepository import InterfaceUserRepository

class AddChannelUseCase:
    def __init__(self, repo: InterfaceChannelRepository, user_repo: InterfaceUserRepository):
        self.repo = repo
        self.user_repo = user_repo

    async def execute(self, title: str, url: str, telegram_id: int):

        user = await self.user_repo.get_by_tg_id(telegram_id)

        if user is None:
            raise UserNotFoundError(telegram_id)

        if not user.is_staff():
            raise NotHavePermissionToAddChannel()
        
        return await self.repo.add_item(title, url, user.id)