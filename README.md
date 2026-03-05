# 🤖 Nurka FAQ и Channel Management API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-11890B?style=for-the-badge&logo=sqlalchemy&logoColor=white)

> Мощный API для управления базой знаний и каналами в Telegram-боте с поддержкой ролевого доступа

## ✨ Особенности

🚀 **Быстро и надежно** - Асинхронная архитектура на FastAPI  
🛡️ **Безопасно** - Ролевая система доступа и аутентификация  
🗄️ **Надежно** - PostgreSQL с полной поддержкой транзакций  
🧹 **Чисто** - Clean Architecture для легкого масштабирования  
⚡ **Умно** - Автоматическая защита от дубликатов  

## 🏗️ Архитектура

```
├── 🌐 API слой (api/)
│   ├── Роуты и валидация данных
│   └── Обработка HTTP запросов
│
├── 📋 Application слой (application/)
│   ├── Use Cases - бизнес логика
│   └── Сценарии использования
│
├── 🎯 Domain слой (domain/)
│   ├── Сущности и интерфейсы
│   └── Бизнес правила
│
└── 🔧 Infrastructure слой (infrastructure/)
    ├── Работа с базой данных
    └── Внешние зависимости
```

## 🎮 Возможности

### 👥 Пользователи
- **Регистрация** по Telegram ID
- **3 роли доступа**: user, moderator, admin
- **Валидация** уникальности username, Telegram ID и phone number
- **Права доступа** для каждой операции

### ❓ FAQ (Часто задаваемые вопросы)
- **Добавление** вопросов с заголовком и ссылкой
- **Просмотр** списка и отдельных вопросов
- **Удаление** (только для модераторов и администраторов)
- **Защита** от дубликатов по заголовку и URL

### 📺 Каналы
- **Управление** каналами с заголовком и ссылкой
- **Просмотр** списка доступных каналов
- **Контроль** доступа к операциям
- **Уникальность** заголовков и URL

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.10+
- PostgreSQL
- pip

### Установка

1. **Клонируйте репозиторий:**
```bash
git clone <https://github.com/Rantaro29/nurka-api>
cd nurka-api
```

2. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

3. **Настройте окружение:**
Создайте файл `.env` в корне проекта:
```env
API_AUTH_TOKEN=ваш_уникальный_токен_для_аутентификации
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
```

4. **Запустите сервер:**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Сервер будет доступен по адресу: http://localhost:8000

## 📚 API Документация

После запуска сервера, документация доступна по адресу:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 🔐 Аутентификация

Все запросы требуют заголовок аутентификации:
```
X-Internal-Token: ваш_токен_из_.env_файла
```

### 👥 Пользователи

#### Получение списка пользователей
```http
GET /user/
```
**Требуемые права:** 🔴 admin

#### Создание пользователя
```http
POST /user/
Content-Type: application/json

{
  "username": "john_doe",
  "telegram_id": 123456789,
  "first_name": "John",
  "last_name": "Doe",
  "phone_number": "+1234567890"
}
```

#### Обновление роли пользователя
```http
POST /user/update
Content-Type: application/json

{
  "admin_id": 987654321,
  "telegram_id": 123456789,
  "role": "moderator"
}
```
**Требуемые права:** 🔴 admin

### ❓ FAQ

#### Добавление FAQ
```http
POST /faq/
Content-Type: application/json

{
  "title": "Как создать аккаунт?",
  "url": "https://example.com/help/create-account"
}
```
**Требуемые права:** 🟡 moderator, 🔴 admin

#### Получение списка FAQ
```http
GET /faq/
```

### 📺 Каналы

#### Добавление канала
```http
POST /channel/
Content-Type: application/json

{
  "title": "Новости компании",
  "url": "https://t.me/company_news"
}
```
**Требуемые права:** 🟡 moderator, 🔴 admin

#### Получение списка каналов
```http
GET /channel/
```

## 🛡️ Система прав доступа

| Операция | User | Moderator | Admin |
|----------|------|-----------|-------|
| Просмотр FAQ | ✅ | ✅ | ✅ |
| Просмотр каналов | ✅ | ✅ | ✅ |
| Добавление FAQ | ❌ | ✅ | ✅ |
| Удаление FAQ | ❌ | ✅ | ✅ |
| Добавление каналов | ❌ | ✅ | ✅ |
| Удаление каналов | ❌ | ✅ | ✅ |
| Просмотр пользователей | ❌ | ❌ | ✅ |
| Управление ролями | ❌ | ❌ | ✅ |

## 🚨 Обработка ошибок

Система возвращает понятные сообщения об ошибках:

- **403 Forbidden** - 🔒 Недостаточно прав для выполнения операции
- **404 Not Found** - ❌ Запрашиваемый объект не найден
- **409 Conflict** - 🔄 Нарушение уникальности (дубликат)
- **400 Bad Request** - ⚠️ Неверные параметры запроса

## 🗄️ База данных

### Схема данных

```sql
-- Пользователи
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(32) UNIQUE,
    role VARCHAR(20) NOT NULL,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64),
    telegram_id BIGINT UNIQUE NOT NULL,
    phone_number VARCHAR(20) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- FAQ
CREATE TABLE faq (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) UNIQUE NOT NULL,
    url VARCHAR(255) UNIQUE NOT NULL,
    moderator_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Каналы
CREATE TABLE channel (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) UNIQUE NOT NULL,
    url VARCHAR(255) UNIQUE NOT NULL,
    moderator_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW()
);
```

## 🔧 Разработка

### Структура проекта
```
nurka-api/
├── api/                    # HTTP слой
│   ├── routers/           # Роуты
│   ├── schemas/           # Pydantic модели
│   └── dependencies/      # Зависимости FastAPI
├── application/           # Слой приложения
│   └── use_cases/         # Бизнес-логика
├── domain/               # Доменный слой
│   ├── entities/         # Сущности
│   ├── interfaces/       # Интерфейсы
│   └── exceptions/       # Исключения
├── infrastructure/       # Инфраструктурный слой
│   ├── database.py       # Настройка БД
│   ├── tables.py         # ORM модели
│   └── services/         # Сервисы
├── main.py              # Точка входа
├── config.py            # Конфигурация
└── requirements.txt     # Зависимости
```

### Тестирование
```bash
# Запуск сервера в режиме разработки
uvicorn main:app --reload --port 8000

# Проверка API через curl
curl -H "X-Internal-Token: ваш_токен" http://localhost:8000/faq/
```

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку с вашим фиксом/фичей
3. Сделайте коммит с понятным описанием
4. Создайте pull request

## 📄 Лицензия

Этот проект распространяется под лицензией [MIT License](LICENSE).

```
MIT License

Copyright (c) 2026 Rantaro29

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Благодарности

Спасибо за использование Nurka API! 🎉

---

**Made with ❤️ for Telegram Bot Development**
