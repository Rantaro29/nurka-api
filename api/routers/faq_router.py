from typing import List
from fastapi import APIRouter, Depends
from api.dependencies.faq import get_faq_use_case, get_faq_list_use_case, add_faq_use_case, delete_faq_use_case

from api.schemas.content_link import FaqLinkDTO, CreateFaqRequest
from api.dependencies.deps import validate_api_token, get_x_tg_id

router = APIRouter(dependencies=[Depends(validate_api_token)])

@router.get("/", response_model = List[FaqLinkDTO])
async def list_faqs(
    use_case = Depends(get_faq_list_use_case)
):
    # Просто запускаем сценарий получения списка
    entities = await use_case.execute()
    return [FaqLinkDTO.from_entity(e) for e in entities]

@router.get("/{id}", response_model = FaqLinkDTO)
async def get_faq_item(
    id: int,
    use_case = Depends(get_faq_use_case)
):

    return FaqLinkDTO.from_entity(await use_case.execute(id))

@router.post("/", response_model = FaqLinkDTO)
async def add_faq_item(
    request: CreateFaqRequest,
    tg_id: int = Depends(get_x_tg_id), # Достаем ID автоматически
    use_case = Depends(add_faq_use_case)
):
    
    return FaqLinkDTO.from_entity(await use_case.execute(request.title, request.url_str, tg_id))

@router.delete("/{id}", response_model = FaqLinkDTO)
async def delete_faq_item(
    id: int,
    tg_id: int = Depends(get_x_tg_id), # Достаем ID автоматически
    use_case = Depends(delete_faq_use_case)
):
    return FaqLinkDTO.from_entity(await use_case.execute(id, tg_id))