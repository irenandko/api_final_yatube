# API_FINAL_YATUBE (last version)

API_Final - финальная версия API для Yatube с использованием авторизациии по JWT токену.

> [!NOTE]
> Python 3.9, Django Rest Framework (DRF)

> [!CAUTION]
> Обязательно используйте виртуальное окружение, чтобы избежать конфликта версий различных библиотек.

## Как запустить проект:

*   Клонировать репозиторий и перейти в него в командной строке:

    ```
    git clone https://github.com/irenandko/api_final_yatube.git
    ```

    ```
    cd api_final_yatube
    ```

*   Создать и активировать виртуальное окружение:

    ```
    python -m venv venv
    ```

    ```
    source venv/Scripts/activate
    ```

*   Установить зависимости из файла requirements.txt:

    ```
    python -m pip install --upgrade pip
    ```

    ```
    pip install -r requirements.txt
    ```

*   Выполнить миграции:

    ```
    python manage.py migrate
    ```

*   Запустить проект:

    ```
    python manage.py runserver
    ```
