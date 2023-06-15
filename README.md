# Описание
Данный проект модификация социальной сети [Yatube](https://github.com/apashovkin48/hw05_final) позволяет авторам вести свой блог, публиковать свои мысли и интересные идеи.
Так же авторы могут подписываться на своих коллег по форуму, которые показались для них наиболее интересными.

# Доступный функционал
- Управление пользователями
- Регистрация пользователей
- Восстановление доступа через электронную почту
- Создание, редактирование постов с изображениями
- Подписка на автора
- Лента с самыми актуальными постами пользователей
- Просмотр ленты постов пользователей

# Для полной информации о работе сервиса ознакомтесь с документацией
```
http://127.0.0.1:8000/redoc/
```

# Устновка
Клонируйте репозиторий на ваш ПК
```
git clone https://github.com/apashovkin48/api_final_yatube.git
```
Перейдите в папку с проектом:
```
cd api_final_yatube
```
Установите виртуальное окружение и активируйте его:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
pip3 install -r requirements.txt
```
Выполнить миграции:
```
cd yatube_api
```
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

# Используемые технолигии
```
- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite3
```

# Примеры запросов API для работы с постами
```
/api/v1/posts/{id}/ (GET, POST, PUT, PATСH, DELETE)
/api/v1/posts/{post_id}/comments/{id} (GET, POST, PUT, PATHC, DELETE)
/api/v1/groups/{id}/ (GET)
/api/v1/follow/ (GET, POST)
```

# Примеры запросов API для работы с правами пользователей
```
/api/v1/jwt/create/ (POST)
/api/v1/jwt/refresh/ (POST)
/api/v1/jwt/verify/ (POST)
```
