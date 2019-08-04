e-lib
====
Тестовое web-приложение по управлению электронной библиотекой.

Установка зависимостей:
```
pip install -r requirements.txt
```
Создание таблиц в БД:
```
$  psql -h localhost -U ivan -d test_lib_db -f init.sql
```
Наполнение наблиц начальными данными:
```
$ psql -h localhost -U ivan -d test_lib_db -f data.sql
```
Данные для входа:
```
user1:pass
user2:pass2
```
