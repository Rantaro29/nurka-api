from fastapi import HTTPException, status

from domain.exceptions.faq import FaqNotFoundError
from domain.interfaces.InterfaceFaqRepository import InterfaceFaqRepository
from domain.entities.content_link import FaqLink

class GetFaqUseCase:
    def __init__(self, repo: InterfaceFaqRepository):
        self.repo = repo

    async def execute(self, item_id: int) -> FaqLink:
        faq = await self.repo.get_item(item_id)

        if faq is None:
            raise FaqNotFoundError(item_id)
        
        return faq
