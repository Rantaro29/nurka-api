from fastapi import Depends
from infrastructure.database import get_db_session
from infrastructure.services.repository.FaqRepository import SQLAlchemyFAQrepository

from application.use_cases.faq.add_faq import AddFaqUseCase
from application.use_cases.faq.get_faq import GetFaqUseCase
from application.use_cases.faq.get_faq_list import GetFaqListUseCase
from application.use_cases.faq.delete_faq import DeleteFaqUseCase

from api.dependencies.auth import get_user_repo

def get_faq_repo(session = Depends(get_db_session)):
    return SQLAlchemyFAQrepository(session)

def get_faq_use_case(repo = Depends(get_faq_repo)):
    return GetFaqUseCase(repo)

def get_faq_list_use_case(repo = Depends(get_faq_repo)):
    return GetFaqListUseCase(repo)

def add_faq_use_case(repo = Depends(get_faq_repo), user_repo = Depends(get_user_repo)):
    return AddFaqUseCase(repo, user_repo)

def delete_faq_use_case(repo = Depends(get_faq_repo), user_repo = Depends(get_user_repo)):
    return DeleteFaqUseCase(repo, user_repo)


