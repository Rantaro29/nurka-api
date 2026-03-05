from domain.interfaces.InterfaceFaqRepository import InterfaceFaqRepository
from domain.interfaces.InterfaceUserRepository import InterfaceUserRepository
from domain.entities.user import User, Role
from domain.exceptions.user import UserNotFoundError
from domain.exceptions.faq import NotHavePermissionToAddFaq

class AddFaqUseCase:
    def __init__(self, repo: InterfaceFaqRepository, user_repo: InterfaceUserRepository):
        self.repo = repo
        self.user_repo = user_repo

    async def execute(self, title: str, url: str, telegram_id: int):

        user = await self.user_repo.get_by_tg_id(telegram_id)

        if user is None:
            raise UserNotFoundError(telegram_id)

        if not user.is_staff():
            raise NotHavePermissionToAddFaq()

        return await self.repo.add_item(title, url, user.id)