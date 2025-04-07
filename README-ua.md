# 🛒 OLX Парсер

English | [Русский](https://github.com/ptmasher/olx-parser/blob/main/README-ru.md) | [Українська](https://github.com/ptmasher/olx-parser/blob/main/README-ua.md)

Python-парсер для оголошень OLX, побудований на базі BeautifulSoup.  
Дозволяє шукати товари, отримувати детальну інформацію про кожне оголошення та розраховувати середню ціну зі сторінки результатів.

## 📦 Встановлення

- Клонувати репозиторій:
```bash
git clone https://github.com/ptmasher/olx-parser.git
```

- Встановити залежності:
```bash
pip install -r requirements.txt
```

## 📚 Залежності

- Python 3.6 або вище  
- lxml  
- beautifulsoup4  
- requests  

## 🖥️ Використання

### Швидкий запуск
```bash
python main.py
```

### Функції

- Отримати сторінку за допомогою `get_page()`
```python
soup = get_page("PlayStation 5", country="BG", currency="BGN", condition="Used")
```

- Розпарсити оголошення та зберегти інформацію через `parse_items()`
```python
parse_items(soup)
```

- Розрахувати середню ціну товарів за допомогою `average_price()`
```python
average_price(soup)
```

### Приклад використання в коді
```python
soup = get_page("Iphone 15", country="UA", currency="USD", condition="used")

parse_items(soup)
avg = average_price(soup)
print(f"Середня ціна: {avg} UAH")
```

## ⚙️ Конфігурація

Налаштування зберігаються у файлі `config.py`:

- `countryDomain` — підтримувані країни (`UA`, `PL` тощо)
- `currencyDict` — доступні валюти (`USD`, `PLN` тощо)
- `conditionDict` — фільтри стану товару (`all`, `new`, `used`)
- CSS-класи для парсингу: `NAME_CLASS`, `PRICE_CLASS` та інші

## 📌 Примітки

Працює з актуальною структурою сайту OLX.

## 🤝 Внесок у проект

Pull-запити вітаються!

Якщо ви знайшли помилку чи баг — [створіть issue](https://github.com/ptmasher/olx-parser/issues) або зв'яжіться зі мною напряму.

Дякую за участь у проекті!

## 📝 Ліцензія

Цей проєкт ліцензований за ліцензією MIT
