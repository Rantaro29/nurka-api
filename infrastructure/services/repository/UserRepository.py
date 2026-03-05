from datetime import datetime
from domain.exceptions.user import UserAlreadyExistsByPhoneNumberError, UserAlreadyExistsError, UserAlreadyExistsByTgIdError
from sqlalchemy.exc import IntegrityError  # <--- Проверь этот импорт!
from domain.entities.user import Role, User as UserModel
from infrastructure.tables import User
from sqlalchemy import select
from domain.interfaces.InterfaceUserRepository import InterfaceUserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from domain.exceptions.user import UserNotFoundError

class SQLAlchemyUserRepository(InterfaceUserRepository):

    def __init__(self, session: AsyncSession): 
        self.session = session

    def _map_to_entity(self, obj: User) -> UserModel:
        return UserModel(
            id = obj.id,
            role = obj.role,
            first_name = obj.first_name,
            telegram_id = obj.telegram_id,
            created_at = obj.created_at,
            username = obj.username,
            last_name = obj.last_name,
            phone_number = obj.phone_number
        )

    async def get_by_tg_id(self, telegram_id):
        # Ищем через select, так как telegram_id — не PK
        query = select(User).where(User.telegram_id == telegram_id)
        result = await self.session.execute(query)
        obj = result.scalar_one_or_none()

        if not obj:
            return None
            
        return self._map_to_entity(obj)

    async def get_role(self, telegram_id):
        query = select(User).where(User.telegram_id == telegram_id)
        result = await self.session.execute(query)
        obj = result.scalar_one_or_none()

        if not obj:
            return None
            
        await self.session.commit()

        return obj.role

    async def update_role(self, telegram_id, new_role):
        query = select(User).where(User.telegram_id == telegram_id)
        result = await self.session.execute(query)
        obj = result.scalar_one_or_none()

        if not obj:
            raise UserNotFoundError(telegram_id)
            
        # 2. Меняем поле
        obj.role = new_role

        # 3. Сохраняем (SQLAlchemy выполнит UPDATE при коммите)
        await self.session.commit()
        await self.session.refresh(obj) # Чтобы вернуть актуальный объект
        return self._map_to_entity(obj)

    async def get_users(self):
        result = await self.session.execute(select(User))
        db_items = result.scalars().all()

        return [self._map_to_entity(item) for item in db_items]

    async def create(self, telegram_id, username, first_name, last_name, phone_number):
    
        user_model = User(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name = last_name,
            phone_number = phone_number,
            role = Role.user,
            created_at = datetime.now()
        )
        
        self.session.add(user_model)

        try:
            await self.session.commit()
            await self.session.refresh(user_model)
            return self._map_to_entity(user_model)
            
        except IntegrityError as e:
            await self.session.rollback()
            error_message = str(e.orig).lower()

            if "users_username_key" in error_message:
                raise UserAlreadyExistsError(username) 
            
            if "users_telegram_id_key" in error_message:
                raise UserAlreadyExistsByTgIdError(telegram_id)
            
            if "users_phone_number_key" in error_message:
                raise UserAlreadyExistsByPhoneNumberError(phone_number)


            raise e

