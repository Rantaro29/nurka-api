
from fastapi import HTTPException, status
from domain.interfaces.InterfaceChannelRepository import InterfaceChannelRepository
from domain.exceptions.channel import ChannelNotFoundError, NotHavePermissionToDeleteChannel
from domain.exceptions.user import UserNotFoundError
from domain.interfaces.InterfaceUserRepository import InterfaceUserRepository

class DeleteChannelUseCase:
    def __init__(self, repo: InterfaceChannelRepository, user_repo: InterfaceUserRepository):
        self.repo = repo
        self.user_repo = user_repo

    async def execute(self, id: int, telegram_id: int):

        channel = await self.repo.get_item(id)

        if channel is None:
            raise ChannelNotFoundError(id)

        user = await self.user_repo.get_by_tg_id(telegram_id)

        if user is None:
            raise UserNotFoundError(telegram_id)

        if not user.is_staff():
            raise NotHavePermissionToDeleteChannel()
        
        
        return await self.repo.delete_item(id)
