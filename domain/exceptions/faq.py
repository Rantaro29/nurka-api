class FaqNotFoundError(Exception):
    def __init__(self, item_id: int):
        super().__init__(f"FAQ с id={item_id} не найден")

class NotHavePermissionToAddFaq(Exception):
    def __init__(self):
        super().__init__("Нет прав для добавления FAQ")

class NotHavePermissionToDeleteFaq(Exception):
    def __init__(self):
        super().__init__(f"У вас нет прав для удаления FAQ") 

class RepositoryError(Exception):
    """Базовое исключение для всех репозиториев."""
    def __init__(self, message: str | None = None):
        super().__init__(message)


class DuplicateFAQTitleError(RepositoryError):
    def __init__(self, title: str):
        super().__init__(f"FAQ с названием '{title}' уже существует.")


class DuplicateFAQUrlError(RepositoryError):
    def __init__(self, url: str):
        super().__init__(f"FAQ с URL '{url}' уже существует.")

