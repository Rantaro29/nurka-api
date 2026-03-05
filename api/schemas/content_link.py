from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl
from domain.entities.content_link import FaqLink, ChannelLink


class BaseContentLinkDTO(BaseModel):
    id: int
    title: str
    url: str
    created_at: datetime

class CreateBaseContentLinkDTO(BaseModel):
    title: str = Field(
        example="Tittle"
    )

    url: HttpUrl = Field(
        example="https://example.com"
    )

    @property
    def url_str(self) -> str:
        return str(self.url)

class FaqLinkDTO(BaseContentLinkDTO):
    @classmethod 
    def from_entity(cls, entity: FaqLink):
 
        return cls(
            id=entity.id,
            title=entity.title,
            url=entity.link,
            created_at=entity.created_at,
        )
    
class CreateFaqRequest(CreateBaseContentLinkDTO):
    pass
    
class ChannelLinkDTO(BaseContentLinkDTO):
    @classmethod 
    def from_entity(cls, entity: ChannelLink):
 
        return cls(
            id=entity.id,
            title=entity.title,
            url=entity.link,
            created_at=entity.created_at,
        )
    
class CreateChannelRequest(CreateBaseContentLinkDTO):
    pass