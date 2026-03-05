from fastapi import APIRouter, Depends
from api.schemas.user import UserDTO, CreateUserDTO
from domain.entities.user import Role, User
from typing import List

from api.dependencies.auth import get_users_use_case, get_user_use_case, create_user_use_case, get_role_by_id, update_role_use_case
from api.dependencies.deps import validate_api_token

router = APIRouter(dependencies=[Depends(validate_api_token)])

@router.get("/", response_model = List[UserDTO])
async def get_users(
    telegram_id: int,
    use_case = Depends(get_users_use_case)
):
    # Просто запускаем сценарий получения списка
    entities = await use_case.execute(telegram_id)
    return [UserDTO.from_entity(e) for e in entities]

@router.post("/", response_model=UserDTO)
async def create_user(
    new_user: CreateUserDTO,
    use_case = Depends(create_user_use_case)
):

    new_user = await use_case.execute(
                    new_user.username,
                    new_user.first_name,
                    new_user.last_name,
                    new_user.telegram_id,
                    new_user.phone_number 
                )
    
    return UserDTO.from_entity(new_user)
    
@router.post("/update", response_model=UserDTO)
async def update_user(
    admin_id: int,
    telegram_id: int,
    role: Role,
    use_case = Depends(update_role_use_case)
):
    
    return await use_case.execute(admin_id, telegram_id, role)
      
@router.get("/{telegram_id}", response_model = UserDTO)
async def get_user_by_id(
    telegram_id: int,
    user_tg_id: int,
    use_case = Depends(get_user_use_case)
):
    return UserDTO.from_entity(await use_case.execute(telegram_id, user_tg_id))
