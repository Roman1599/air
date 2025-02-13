# PDF to JSON Converter

Этот проект читает PDF-файлы и конвертирует данные в JSON.

## Установка
1. Установите зависимости:
pip install -r requirements.txt
2. Запустите обработку:
python main.py

## Описание работы
1. Функция `extract_pdf_data()` извлекает данные из PDF.
2. Конечный JSON выводится в консоль.

## Пример вывода
```json
{
 "PN": "tst",
 "SN": "123123",
 "DESCRIPTION": "PART"
}
