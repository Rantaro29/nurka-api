from abc import ABC, abstractmethod
from typing import List
from domain.entities.content_link import ChannelLink

class InterfaceChannelRepository(ABC):  

    @abstractmethod
    async def get_list_items(self) -> List[ChannelLink]:

        pass

    @abstractmethod
    async def add_item(self,  x_tg_id: int, title: str, url: str, moderator_id: str = 1) -> ChannelLink:
        
        pass

    @abstractmethod
    async def delete_item(self, id: int) -> ChannelLink:

        pass

    @abstractmethod
    async def get_item(self, item_id: int) -> ChannelLink:

        pass
