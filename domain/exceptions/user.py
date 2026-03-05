class UserNotFoundError(Exception):
    def __init__(self, item_id: int):
        super().__init__(f"User с id={item_id} не найден")

class RepositoryError(Exception):
    """Базовое исключение для всех репозиториев."""
    def __init__(self, message: str | None = None):
        super().__init__(message)

class NotHavePermissionToDeleteUser(Exception):
    def __init__(self):
        super().__init__(f"У вас нет прав для удаления User") 

class NotHavePermissionToGetUser(Exception):
    def __init__(self):
        super().__init__(f"У вас нет прав для просмотра User") 

class NotHavePermissionToUpdateUser(Exception):
    def __init__(self):
        super().__init__(f"У вас нет прав для обновления роли User") 


class NotHavePermissionToGetUsers(Exception):
    def __init__(self):
        super().__init__(f"У вас нет прав для просмотра Users") 

class UserAlreadyExistsError(Exception):
    def __init__(self, username):
        self.username = username
        super().__init__(f"Username '{username}' уже занят")

class UserAlreadyExistsByTgIdError(Exception):
    def __init__(self, tg_id):
        self.tg_id = tg_id
        super().__init__(f"User с Telegram ID {tg_id} уже есть")

class UserAlreadyExistsByPhoneNumberError(Exception):
    def __init__(self, phone_number):
        self.phone_number = phone_number
        super().__init__(f" пользователь с таким Phone Number {phone_number} уже есть")
 