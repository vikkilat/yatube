# Проект социальной сети Yatube для блогеров
[![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)](https://github.com/EvgVol)
[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/-Bootstrap-464646??style=flat-square&logo=Bootstrap)](https://www.getbootstrap.com/)
[![HTML](https://img.shields.io/badge/-HTML-464646??style=flat-square&logo=HTML)]()
[![CSS](https://img.shields.io/badge/-CSS-464646??style=flat-square&logo=CSS)]()
[![Unittest](https://img.shields.io/badge/-Unittest-464646??style=flat-square&logo=Unittest)]()

Yatube - социальная сеть, даёт пользователям возможность создать учётную запись,
публиковать посты, создавать группы, оставлять комментарии и подписываться на
любимых авторов.

## Описание проекта:

В проекте социальная сеть Yatube реализованы следующие функции:

* регистрация новых пользователей;
* изменение и восстановления пароля через email;
* добавление/удаление текстовых постов, постов с картинками и возможность
присвоить пост к тематической группе;
* редактирование постов только его автором;
* возможность пользователям оставлять комментарии к постам;
* подписка/отписка на понравившихся авторов;
* создание тематических групп;
* создание отдельной ленты с постами авторов, на которых подписан пользователь;
* создание отдельной ленты постов по группам.

## Покрытие тестами:

Покрытие тестами выполнено при помощи ```Unittest```. Каждому тесту соответствует
отдельный файл. Тесты покрывают следующие области:
* тесты кэширования страниц;
* тесты комментариев;
* тесты подписок на авторов;
* тесты форм;
* тесты загрузки изображений;
* тесты моделей базы данных;
* тесты URL проекта;
* тесты view функций.

## Стек технологий:

*   Python
*   Django
*   SQLite
*   HTML
*   CSS
*   Unittest
*   Bootstrap

## Как запустить проект:

* Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:vikkilat/yatube.git
```

```
cd yatube
```

* Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
venv/scripts/activate
```

* Установить зависимости из файла ```requirements.txt```:

```
pip install -r requirements.txt
```

* Выполнить миграции:

```
python manage.py migrate
```

* Создать суперпользователя:
```
python manage.py createsuperuser
```
* Запустить проект:

```
python manage.py runserver
```
После создания суперпользователя и запуска проекта, вам будет доступна админка
```/admin```, из которой можно управлять проектом, добавлять и удалять группы, посты,
пользователей и т.д.

* Тесты запускаются командой:
```
python manage.py test
```
## Автор:
[Латышева Виктория](https://github.com/vikkilat)
