class ChannelNotFoundError(Exception):
    def __init__(self, item_id: int):
        super().__init__(f"Channel с id={item_id} не найден")

class RepositoryError(Exception):
    """Базовое исключение для всех репозиториев."""
    def __init__(self, message: str | None = None):
        super().__init__(message)

class NotHavePermissionToAddChannel(Exception):
    def __init__(self):
        super().__init__("Нет прав для добавления Channel")

class NotHavePermissionToDeleteChannel(Exception):
    def __init__(self):
        super().__init__(f"У вас нет прав для удаления Channel") 

class DuplicateChannelTitleError(RepositoryError):
    def __init__(self, title: str):
        super().__init__(f"Channel с названием '{title}' уже существует.")


class DuplicateChannelUrlError(RepositoryError):
    def __init__(self, url: str):
        super().__init__(f"Channel с URL '{url}' уже существует.")

