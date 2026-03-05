import secrets
from fastapi import HTTPException, Header
from config import settings

# 1. Добавляем Header(...) в аргументы, чтобы FastAPI понял, откуда брать данные
# 2. Используем secrets.compare_digest для безопасного сравнения
def validate_api_token(x_internal_token: str = Header(..., alias="X-Internal-Token")):
    if not secrets.compare_digest(x_internal_token, settings.API_AUTH_TOKEN):
        raise HTTPException(status_code=403, detail="Forbidden")
    return True

def get_x_tg_id(x_tg_id: int = Header(..., description="ID пользователя Telegram")):
    # Здесь можно добавить проверку: если ID слишком короткий или отрицательный
    if x_tg_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid Telegram ID")
    return x_tg_id