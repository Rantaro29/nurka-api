from domain.interfaces.InterfaceFaqRepository import InterfaceFaqRepository

class GetFaqListUseCase:
    def __init__(self, repo: InterfaceFaqRepository):
        self.repo = repo

    async def execute(self):
        # Просто запрашиваем список
        return await self.repo.get_list_items()
