# PostgreSQL Data Transfer

PostgreSQL Data Transfer - это инструмент на Python для перекачки данных между двумя базами данных PostgreSQL. Это может быть полезно при миграции данных, резервном копировании или создании тестовых окружений.

## Особенности
- Поддержка перекачки данных между различными PostgreSQL серверами
- Автоматическое определение структуры таблицы
- Простой и понятный код на Python для легкой модификации и доработки

## Требования
- Python 3.6 или выше
- psycopg2

## Установка
1. Клонируйте репозиторий:
git clone https://github.com/SirDeadCat/PostgreSQLDataTransfer.git
2. Установите зависимости:
pip install psycopg2

## Использование
Импортируйте функцию `transfer_data` из файла `datatransfer.py` и вызовите её с соответствующими параметрами, такими как исходная и целевая строка соединения и имя таблицы.

Пример использования:
```python
from datatransfer import transfer_data

source_connection_string = "host='source_host' dbname='source_db' user='user' password='password'"
destination_connection_string = "host='destination_host' dbname='destination_db' user='user' password='password'"
table_to_transfer = "table_name"

transfer_data(source_connection_string, destination_connection_string, table_to_transfer)
