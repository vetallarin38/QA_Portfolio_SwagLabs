import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_test():
    print("🚀 Починаємо тест...")
    
    # 1. Запускаємо Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # 2. Відкриваємо сайт
        driver.get("https://www.saucedemo.com/")
        print("✅ Сайт відкрито")

        # 3. Логін
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Перевірка, що зайшли (чекаємо появи списку товарів)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
        print("✅ Логін успішний")

        # 4. Додаємо рюкзак у кошик
        add_btn = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_btn.click()
        print("✅ Товар додано в кошик")

        # 5. Йдемо в кошик
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # 6. Тиснемо Checkout
        driver.find_element(By.ID, "checkout").click()

        # 7. Заповнюємо форму
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        # 8. Фініш
        driver.find_element(By.ID, "finish").click()

        # 9. Перевірка фінального повідомлення
        success_text = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert "Thank you for your order!" in success_text
        print("🎉 ТЕСТ ПРОЙШОВ УСПІШНО! Замовлення оформлено.")

    except Exception as e:
        print(f"❌ Помилка: {e}")
    
    finally:
        # Закриваємо браузер через 5 секунд, щоб ти встиг побачити результат
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    run_test()