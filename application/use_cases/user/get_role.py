from domain.interfaces.InterfaceUserRepository import InterfaceUserRepository

class GetRoleByIdUseCase:
    def __init__(self, repo: InterfaceUserRepository):
        self.repo = repo

    async def execute(self, telegram_id: int):
        return await self.repo.get_role(telegram_id)