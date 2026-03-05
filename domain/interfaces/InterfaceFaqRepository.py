from abc import ABC, abstractmethod
from typing import List
from domain.entities.content_link import FaqLink

class InterfaceFaqRepository(ABC):  

    @abstractmethod
    async def get_list_items(self) -> List[FaqLink]:

        pass

    @abstractmethod
    async def add_item(self, title: str, url: str) -> FaqLink:
        
        pass

    @abstractmethod
    async def delete_item(self, id: int) -> FaqLink:
        
        pass

    @abstractmethod
    async def get_item(self, item_id: int) -> FaqLink | None:

        pass
