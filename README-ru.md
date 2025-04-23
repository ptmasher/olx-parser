# 🛒 OLX Парсер

English | [Русский](https://github.com/ptmasher/olx-parser/blob/main/README-ru.md) | [Українська](https://github.com/ptmasher/olx-parser/blob/main/README-ua.md)

Python-парсер для объявлений OLX, построенный с использованием BeautifulSoup.  
Позволяет выполнять поиск товаров, извлекать подробную информацию о каждом объявлении и рассчитывать среднюю цену с основной страницы результатов.

## 📦 Установка

- Клонировать репозиторий:
```bash
git clone https://github.com/ptmasher/olx-parser.git
```

- Установить зависимости:
```bash
pip install -r requirements.txt
```

## 📚 Зависимости

- Python 3.6 или выше  
- lxml  
- beautifulsoup4  
- requests  

## 🖥️ Использование

### Быстрый запуск
```bash
python main.py
```

### Функции

- Получить страницу с помощью функции `get_page()`
```python
soup = get_page("PlayStation 5", country="Bulgaria", currency="BGN", condition="Used")
```

- Распарсить объявления и сохранить информацию с помощью `parse_items()`
```python
parse_items(soup)
```

- Посчитать среднюю цену всех товаров на странице с помощью `average_price()`
```python
average_price(soup)
```

### Пример использования в коде
```python
soup = get_page("Iphone 15", country="Ukraine", currency="USD", condition="used")

parse_items(soup)
avg = average_price(soup)
print(f"Средняя цена: {avg} USD")
```

## ⚙️ Конфигурация

Настройки находятся в файле `config.py`:

- `countryDomain` — поддерживаемые страны (`Ukraine`, `Poland` и т.д.)
- `currencyDict` — доступные валюты (`USD`, `PLN` и т.д.)
- `conditionDict` — фильтры состояния товара (`all`, `new`, `used`)
- CSS-классы для парсинга: `NAME_CLASS`, `PRICE_CLASS` и др.

## 📌 Примечания

Работает с текущей структурой сайта OLX.

## 🤝 Вклад в проект

Pull-реквесты приветствуются!

Если вы нашли ошибку или баг — [создайте issue](https://github.com/ptmasher/olx-parser/issues) или напишите мне напрямую.

Спасибо за участие в проекте!

## 📝 Лицензия

Этот проект лицензирован по лицензии MIT