Простой ToDo менеджер, реализованный на веб-фреймворке Django
В качестве веб-интерфейса использован фреймворк Semantic UI https://semantic-ui.com/

Создаем папку для нового проекта и переходим в нее

    md ToDoDjango & cd ToDoDjango


Устанавливаем и активируем виртуальное окружение

    python3 -m venv venv
    . venv/bin/activate


Инициализируем git

    git init


Устанавливаем модули

    pip install django


Создаем проект todoapp и переходим в него

    django-admin startproject todoapp & cd todoapp

Создадим приложение todolist

    python manage.py startapp todolist

Зарегистрируем приложение в файле settings.py

    INSTALLED_APPS = [
    ...,
    todolist,
]

Добавим папку шаблонов в settings.py

    TEMPLATES = [
    {...,
    'DIRS': ['templates'],
    }]

Структура файлов и папок

    md templates
    mkdir todolist\static\css
    echo .> .gitignore
    echo .> templates/layout.html
    echo .> templates/index.html
    echo .> todolist/static/css/style.css
    echo .> README.MD
    echo .> todolist/urls.py


Создаем файл с зависимостями проекта

    pip freeze > requirements.txt


Запускаем сервер

    python manage.py runserver



Ссылка на оригинал: https://youtu.be/3vfum74ggHE
    
    Терехов Михаил 2022 год