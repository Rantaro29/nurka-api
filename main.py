# main.py
from fastapi import FastAPI, Request, routing, APIRouter, status
from fastapi.responses import JSONResponse

from api.routers.faq_router import router as faq_router
from api.routers.channel_router import router as channel_router
from api.routers.user_router import router as user_router

from domain.exceptions.faq import NotHavePermissionToDeleteFaq, NotHavePermissionToAddFaq, DuplicateFAQTitleError, DuplicateFAQUrlError, FaqNotFoundError
from domain.exceptions.channel import DuplicateChannelTitleError, DuplicateChannelUrlError, ChannelNotFoundError, NotHavePermissionToAddChannel, NotHavePermissionToDeleteChannel
from domain.exceptions.user import UserAlreadyExistsByTgIdError, UserAlreadyExistsError, UserNotFoundError,  NotHavePermissionToGetUser, NotHavePermissionToDeleteUser, NotHavePermissionToUpdateUser, UserAlreadyExistsByPhoneNumberError


app = FastAPI(title="FAQ Service")

# Регистрируем роутеры
app.include_router(faq_router, prefix="/faq", tags=["FAQ"])
app.include_router(channel_router, prefix="/channel", tags=["CHANNEL"])
app.include_router(user_router,prefix="/user", tags=["USER"])

@app.exception_handler(NotHavePermissionToUpdateUser)
@app.exception_handler(NotHavePermissionToGetUser)
@app.exception_handler(NotHavePermissionToAddChannel)
@app.exception_handler(NotHavePermissionToDeleteChannel)
@app.exception_handler(NotHavePermissionToDeleteFaq)
@app.exception_handler(NotHavePermissionToAddFaq)
async def permission_exception_handler(request: Request, exc: NotHavePermissionToAddFaq):
    return JSONResponse(
        status_code=403,
        content={"detail": "У вас недостаточно прав для выполнения этого действия"}
    )

@app.exception_handler(UserNotFoundError)
@app.exception_handler(ChannelNotFoundError)
@app.exception_handler(FaqNotFoundError)
async def not_found_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        # Достаем сообщение прямо из исключения
        content={"detail": str(exc)} 
    )


@app.exception_handler(DuplicateChannelTitleError)
@app.exception_handler(DuplicateChannelUrlError)
@app.exception_handler(DuplicateFAQTitleError)
@app.exception_handler(DuplicateFAQUrlError)
async def faq_conflict_exception_handler(request: Request, exc: Exception):
    # Мы можем достать текст ошибки, который ты сформировал в репозитории
    return JSONResponse(

        status_code=status.HTTP_409_CONFLICT,
        content={"detail": str(exc)} 
    )

@app.exception_handler(UserAlreadyExistsByTgIdError)
@app.exception_handler(UserAlreadyExistsByPhoneNumberError)
@app.exception_handler(UserAlreadyExistsError)
async def user_already_exists_handler(request: Request, exc: UserAlreadyExistsError):
    return JSONResponse(
        status_code=409,  # Conflict
        content={"detail": str(exc)}
    )
