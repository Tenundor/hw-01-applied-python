# hw-01-applied-python

Homework number 1 for the course "Applied Python" for the master's program "Machine Learning and High-Load Systems" HSE.

## Задание 1

Соберите всю информацию о клиентах в одну таблицу, где одна строчка соответствует полной информации об одном клиенте.

## Задание 2

При помощи инструмента Streamlit проведите разведочный анализ данных. В него может входить:

- построение графиков распределений признаков
- построение матрицы корреляций
- построение графиков зависимостей целевой переменной и признаков

## Установка и запуск

- клонировать репозиторий
- перейти в директорию с проектом
- активировать виртуальное окружение `poetry shell`
- установить `PostrgreSQL`
- создать новую базу данных `<db_name>`
- создать пользователя `<user>` с паролем `<password>`
- в корне проекта создать файл `.env`
- добавить в файл `.env` строку `DATABASE_URL=postgresql+psycopg2://<user>:<password>@localhost/<db_name>`, где указать актуальные данные по созданной ранее базе данных
- запустить миграцию базы данных `alembic upgrade head`
- запустить скрипт для наполнения БД из csv файлов `python load_data_from_csv_to_db.py`
- запустить скрипт для агрегации данных по клиентам `python aggregate_and_save_agreement_summary.py`
- запустить streamlit приложение `streamlit run streamlit_app.py`
