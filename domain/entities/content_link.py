from datetime import datetime
from dataclasses import dataclass
from enum import Enum


@dataclass
class BaseContentLink:
    id: int
    title: str
    link: str
    moderator_id: int
    created_at: datetime

@dataclass
class FaqLink(BaseContentLink):
    pass

@dataclass
class ChannelLink(BaseContentLink):
    pass

