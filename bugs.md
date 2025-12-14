ug Reports for SwagLabs Store

**Project:** SwagLabs E-commerce  
**Tool used:** Atlassian Jira  
**Author:** Vitalii

# 📊 Summary
Всього знайдено:10 багів Критичних (Critical/Blocker): 3 Середніх (Major): 4 Низьких (Minor/Trivial): 3

# 📸 Proof of Work (Jira Screenshots)
Я оформив усі баги в системі Jira. Ось як виглядає моя дошка та приклад оформленого тікета:
# Jira Kanban Board
![Jira Board](screenshots/jira_board.png)

# Bug Report Example (Inside Jira)
![Jira Bug Example](screenshots/jira_bug_example.png)

# 📝 Detailed Bug List (Export)

Нижче наведено список знайдених дефектів.
*(Примітка: ID багів відповідають внутрішній нумерації в Jira)*

# [High] Broken product images on Inventory page
**Description:** Зображення товарів не завантажуються для користувача `problem_user`. Замість фото відображається заглушка з собакою.
**Steps to Reproduce:**
  1. Log in as `problem_user`.
  2. Go to Inventory page.
**Actual Result:** Images are broken (404 error visualization).
**Expected Result:** Proper product images should be displayed.

# [Critical] Wrong Item added to Cart
**Description:** При спробі додати "Sauce Labs Bolt T-Shirt", в кошик потрапляє інший товар.

# [Minor] Sorting 'Name (Z to A)' does not work
**Description:** Сортування товарів не змінює порядок списку при виборі опції "Name (Z to A)".
**Actual Result:** Items remain sorted by A-Z.
**Expected Result:** Items should be sorted alphabetically descending (Test.allTheThings() T-Shirt first).

# [Major] Cannot remove items from Cart on Inventory Page
**Description:** Натискання кнопки "Remove" на сторінці каталогу не видаляє товар і не змінює кнопку назад на "Add to cart".

# [Major] Last Name input field is mandatory but accepts empty value
**Location** Checkout: Your Information step.
**Description:** Користувач може перейти до кроку "Overview", залишивши поле "Last Name" пустим (для problem_user валідація зламана).

# [Trivial] Typo in the Footer
**Description:** В футері замість 2024 року стоїть старий рік (або інша візуальна помилка, якщо знайдеш). Примітка: для problem_user футер може бути взагалі обрізаний.

# [Minor] Detail Page shows wrong description
**Steps** Click on "Sauce Labs Fleece Jacket".
**Actual** Description matches "Sauce Labs Backpack".

# [Blocker] Continue' button on Checkout redirects to Home
**Description:** (Гіпотетичний баг для портфоліо) При натисканні Continue відбувається редірект на сторінку логіну замість Step 2.

# [Minor (Performance)] Login Performance Issue
**Description:**  Логін займає більше 5 секунд для користувача performance_glitch_user.
**Actual** >5000ms.
**Expected** <1000ms.

# [Critical] XSS Vulnerability in First Name field (Hypothetical)
**Description:** Введення <script>alert(1)</script> у поле First Name викликає алерт на сторінці Overview.