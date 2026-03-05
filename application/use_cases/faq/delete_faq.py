from domain.exceptions.faq import FaqNotFoundError, NotHavePermissionToDeleteFaq
from domain.exceptions.user import UserNotFoundError
from domain.interfaces.InterfaceFaqRepository import InterfaceFaqRepository
from domain.interfaces.InterfaceUserRepository import InterfaceUserRepository
from domain.entities.user import Role


class DeleteFaqUseCase:
    def __init__(self, repo: InterfaceFaqRepository, user_repo: InterfaceUserRepository):
        self.repo = repo
        self.user_repo = user_repo

    async def execute(self, id: int, telegram_id: int):

        faq = await self.repo.get_item(id)

        if faq is None:
            raise FaqNotFoundError(id)

        user = await self.user_repo.get_by_tg_id(telegram_id)

        if user is None:
            raise UserNotFoundError(telegram_id)

        if not user.is_staff():
            raise NotHavePermissionToDeleteFaq()
        
        
        return await self.repo.delete_item(id)
    