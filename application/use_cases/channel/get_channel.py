from fastapi import HTTPException, status
from domain.exceptions.faq import DuplicateFAQTitleError, DuplicateFAQUrlError, FaqNotFoundError
from domain.interfaces.InterfaceChannelRepository import InterfaceChannelRepository
from domain.entities.content_link import FaqLink
from domain.exceptions.channel import ChannelNotFoundError

class GetChannelUseCase:
    def __init__(self, repo: InterfaceChannelRepository):
        self.repo = repo

    async def execute(self, item_id: int) -> FaqLink:
  
        channel = await self.repo.get_item(item_id)

        if channel is None:
            raise ChannelNotFoundError(item_id)
        
        return channel
