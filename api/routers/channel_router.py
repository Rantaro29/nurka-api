from typing import List
from fastapi import APIRouter, Depends, Header
from api.dependencies.channel import get_channel_list_use_case, get_channel_use_case, add_channel_use_case, delete_channel_use_case
from api.schemas.content_link import CreateChannelRequest, ChannelLinkDTO
from api.dependencies.deps import validate_api_token, get_x_tg_id

router = APIRouter(dependencies=[Depends(validate_api_token)])


@router.get("/", response_model = List[ChannelLinkDTO])
async def list_faqs(
    use_case = Depends(get_channel_list_use_case)
):
    # Просто запускаем сценарий получения списка
    entities = await use_case.execute()
    return [ChannelLinkDTO.from_entity(e) for e in entities]

@router.get("/{id}", response_model = ChannelLinkDTO)
async def get_faq_item(
    id: int,
    use_case = Depends(get_channel_use_case)
):

    return ChannelLinkDTO.from_entity(await use_case.execute(id))

@router.post("/", response_model = ChannelLinkDTO)
async def add_faq_item(
    request: CreateChannelRequest,
    tg_id: int = Depends(get_x_tg_id), # Достаем ID автоматически
    use_case = Depends(add_channel_use_case)
):
    
    return ChannelLinkDTO.from_entity(await use_case.execute(request.title, request.url_str, tg_id))

@router.delete("/{id}", response_model = ChannelLinkDTO)
async def delete_faq_item(
    id: int,
    tg_id: int = Depends(get_x_tg_id), # Достаем ID автоматически
    use_case = Depends(delete_channel_use_case)
):
    return ChannelLinkDTO.from_entity(await use_case.execute(id, tg_id))