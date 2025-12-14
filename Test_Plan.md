Project: Swag Labs E-commerce Version: 1.0 QA Engineer: [Твоє Ім'я]

1. Introduction (Вступ)
Мета цього плану — визначити стратегію тестування веб-магазину Swag Labs для забезпечення стабільності функціоналу покупки товарів.

2. In Scope (Що тестуємо)
Функціонал:

Сторінка авторизації (Login).

Каталог товарів (Inventory): сортування, відображення.

Кошик (Cart): додавання, видалення.

Оформлення замовлення (Checkout): введення даних, фініш.

Браузери: Google Chrome (Latest), Firefox.

3. Out of Scope (Що НЕ тестуємо)
Мобільний додаток.

Продуктивність (Load Testing) — в цій ітерації.

Безпека (SQL Injection) — оскільки це демо-сайт.

4. Test Strategy (Стратегія)
Smoke Testing: Перевірка критичного шляху (Login -> Buy Item) після кожного деплою.

Functional Testing: Перевірка сортування, валідації полів.

UI Testing: Перевірка відповідності картинок товарам.

5. Tools (Інструменти)
Bug Tracking: Jira (або GitHub Issues).

Browser: Chrome DevTools.

Automation: Python + Selenium.

API Testing: Postman.

6. Entry & Exit Criteria
Start: Білд доступний за посиланням saucedemo.com.

Stop: Усі блокуючі (Blocker) та критичні (Critical) баги виправлені. Pass Rate тест-кейсів > 90%.
