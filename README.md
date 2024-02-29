# Web Scraping Tool

## Описание
Этот инструмент предназначен для извлечения контрактных адресов из мета-тегов веб-страниц. Он позволяет обработать список URL-ов и сохранить результаты в два файла: `contract.txt` (детали запросов) и `list.txt` (контрактные адреса).

## Использование

### Установка зависимостей
```bash
pip install -r requirements.txt
```

## Запуск
Укажите URL-ы в файле urls.txt.
Запустите скрипт main.py
```bash
python main.py
```

## Результаты
- contract.txt: Детали запросов к каждому URL-у.
- list.txt: Контрактные адреса, разделенные запятой, каждый на новой строке. Можно вставлять в ваш скрипт.

# Web Scraping Tool

## Description
This tool is designed to extract contract addresses from meta tags on web pages. It allows processing a list of URLs and saving the results in two files: contract.txt (details of the requests) and list.txt (contract addresses).

## Usage
### Install Dependencies
```bash
pip install -r requirements.txt
```

## Run
Specify the URLs in the urls.txt file.
Run the main.py script.
```bash
python main.py
```

## Results
- contract.txt: Details of the requests for each URL.
- list.txt: Contract addresses, separated by commas, each on a new line.