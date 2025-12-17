# SQL Queries Portfolio

Тут зібрані приклади SQL-запитів, які я використовую для роботи з базами даних (PostgreSQL / MySQL).
Ці запити демонструють навички вибірки, фільтрації, агрегації та з'єднання таблиць.

---

### 1. Пошук активних користувачів (WHERE + ORDER BY)
**Задача:** Знайти всіх користувачів, які зареєструвалися у 2024 році та мають активний статус. Відсортувати від нових до старих.

```sql
SELECT id, username, email, created_at
FROM users
WHERE status = 'active'
  AND created_at >= '2024-01-01'
ORDER BY created_at DESC;
2. Аналіз замовлень клієнта (INNER JOIN)
Задача: Отримати список усіх замовлень разом з іменами клієнтів та датами замовлень.

SQL

SELECT
    users.username AS client_name,
    orders.id AS order_id,
    orders.total_amount,
    orders.order_date
FROM orders
JOIN users ON orders.user_id = users.id;
3. Пошук "покинутих" кошиків (LEFT JOIN + IS NULL)
Задача: Знайти користувачів, які зареєструвалися, але ніколи не робили замовлень.

SQL

SELECT users.username, users.email
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE orders.id IS NULL;
4. Статистика продажів по містах (AGGREGATION)
Задача: Порахувати кількість замовлень та загальну суму продажів для кожного міста. Показати тільки ті міста, де сума продажів більше 10 000.

SQL

SELECT
    shipping_city,
    COUNT(id) AS total_orders,
    SUM(total_amount) AS total_revenue
FROM orders
GROUP BY shipping_city
HAVING SUM(total_amount) > 10000
ORDER BY total_revenue DESC;
5. Оновлення даних (UPDATE)
Задача: Підняти ціну на 10% для всіх товарів категорії "Electronics".

SQL

UPDATE products
SET price = price * 1.10
WHERE category = 'Electronics';
