from datetime import datetime
import os
from sqlalchemy import select
from domain.exceptions.channel import ChannelNotFoundError
from domain.entities.content_link import ChannelLink
from domain.interfaces.InterfaceChannelRepository import InterfaceChannelRepository
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.tables import Channel
from sqlalchemy.exc import IntegrityError
from domain.exceptions.channel import DuplicateChannelTitleError, DuplicateChannelUrlError, ChannelNotFoundError
from dotenv import load_dotenv


class SQLAlchemyChannelRepository(InterfaceChannelRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    def _map_to_entity(self, obj: Channel) -> ChannelLink:
        return ChannelLink(
            id=obj.id,
            title=obj.title,
            link=obj.url,
            moderator_id=obj.moderator_id,
            created_at=obj.created_at
        )

    async def get_list_items(self):
        result = await self.session.execute(select(Channel))
        db_items = result.scalars().all()

        return [self._map_to_entity(item) for item in db_items]


    async def add_item(self, title: str, url: str, telegram_id: str = 1):

        channel_model = Channel(
            title=title,
            url=url,
            moderator_id = telegram_id,
            created_at = datetime.now()
        )
        
        self.session.add(channel_model)

        try:
            await self.session.commit()
            await self.session.refresh(channel_model)
            return self._map_to_entity(channel_model)
            
        except IntegrityError as e:
            await self.session.rollback()
            error_message = str(e.orig).lower()

            if "channel_title_key" in error_message:
                raise DuplicateChannelTitleError(title)  # <-- передаем title
            if "channel_url_key" in error_message:
                raise DuplicateChannelUrlError(url)      # <-- передаем url

            raise

    async def delete_item(self, id):
        obj = await self.session.get(Channel, id)

        if not obj:
            raise None
            
        await self.session.delete(obj)
        await self.session.commit()

        return self._map_to_entity(obj)

    async def get_item(self, item_id):
        obj = await self.session.get(Channel, item_id)

        await self.session.commit()

        if not obj:
            return None

        return self._map_to_entity(obj)

