from domain.interfaces.InterfaceChannelRepository import InterfaceChannelRepository

class GetChannelListUseCase:
    def __init__(self, repo: InterfaceChannelRepository):
        self.repo = repo

    async def execute(self):
        # Просто запрашиваем список
        return await self.repo.get_list_items()
