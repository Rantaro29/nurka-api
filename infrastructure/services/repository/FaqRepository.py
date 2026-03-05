from typing import List
from domain.exceptions.faq import FaqNotFoundError, DuplicateFAQTitleError, DuplicateFAQUrlError, RepositoryError
from domain.interfaces.InterfaceFaqRepository import InterfaceFaqRepository
from infrastructure.database import AsyncSessionLocal
from datetime import datetime
from infrastructure.tables import FAQ
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from domain.entities.content_link import FaqLink


class SQLAlchemyFAQrepository(InterfaceFaqRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    def _map_to_entity(self, obj: FAQ) -> FaqLink:
        return FaqLink(
            id=obj.id,
            title=obj.title,
            link=obj.url,
            moderator_id=obj.moderator_id,
            created_at=obj.created_at
        )

    async def get_item(self, item_id: int) -> FaqLink | None:
        obj = await self.session.get(FAQ, item_id)

        await self.session.commit()

        if not obj:
            return None

        return self._map_to_entity(obj)
        
    async def get_list_items(self) -> List[FaqLink]:
        result = await self.session.execute(select(FAQ))
        db_items = result.scalars().all()

        return [self._map_to_entity(item) for item in db_items]

    async def add_item(self, title: str, url: str, telegram_id: int) -> FaqLink:

        faq_model = FAQ(
            title=title,
            url=url,
            moderator_id = telegram_id,
            created_at = datetime.now()
        )
        
        self.session.add(faq_model)

        try:
            await self.session.commit()
            await self.session.refresh(faq_model)
            return self._map_to_entity(faq_model)
            
        except IntegrityError as e:
            await self.session.rollback()
            error_message = str(e.orig).lower()

            if "faq_title_key" in error_message:
                raise DuplicateFAQTitleError(title)  # <-- передаем title
            if "faq_url_key" in error_message:
                raise DuplicateFAQUrlError(url)      # <-- передаем url

            raise
            
    async def delete_item(self, item_id: int) -> FaqLink:
        obj = await self.session.get(FAQ, item_id)

        await self.session.delete(obj)
        await self.session.commit()

        return self._map_to_entity(obj)

