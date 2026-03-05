from fastapi import Depends
from infrastructure.database import get_db_session
from infrastructure.services.repository.ChannelRepository import SQLAlchemyChannelRepository

from application.use_cases.channel.add_channel import AddChannelUseCase
from application.use_cases.channel.get_channel import GetChannelUseCase
from application.use_cases.channel.delete_channel import DeleteChannelUseCase
from application.use_cases.channel.get_channel_list import GetChannelListUseCase

from api.dependencies.auth import get_user_repo

def get_channel_repo(session = Depends(get_db_session)):
    return SQLAlchemyChannelRepository(session)

def get_channel_use_case(repo = Depends(get_channel_repo)):
    return GetChannelUseCase(repo)

def add_channel_use_case(repo = Depends(get_channel_repo), user_repo = Depends(get_user_repo)):
    return AddChannelUseCase(repo, user_repo)

def delete_channel_use_case(repo = Depends(get_channel_repo), user_repo = Depends(get_user_repo)):
    return DeleteChannelUseCase(repo, user_repo)

def get_channel_list_use_case(repo = Depends(get_channel_repo)):
    return GetChannelListUseCase(repo)