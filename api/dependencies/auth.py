from fastapi import Depends
from infrastructure.database import get_db_session
from infrastructure.services.repository.UserRepository import SQLAlchemyUserRepository

from application.use_cases.user.get_users import GetUsersUseCase
from application.use_cases.user.get_by_tg_id import GetUserByIdUseCase
from application.use_cases.user.create_user import CreateUserUseCase
from application.use_cases.user.get_role import GetRoleByIdUseCase
from application.use_cases.user.update_role import UpdateRoleUseCase

def get_user_repo(session = Depends(get_db_session)):
    return SQLAlchemyUserRepository(session)

def get_users_use_case(repo = Depends(get_user_repo)):
    return GetUsersUseCase(repo)

def get_user_use_case(repo = Depends(get_user_repo)):
    return GetUserByIdUseCase(repo)

def create_user_use_case(repo = Depends(get_user_repo)):
    return CreateUserUseCase(repo)

def get_role_by_id(repo = Depends(get_user_repo)):
    return GetRoleByIdUseCase(repo)

def update_role_use_case(repo = Depends(get_user_repo)):
    return UpdateRoleUseCase(repo)

