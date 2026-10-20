
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Open Library Management
    driver.get(
        "file:///C:/Users/Admin/Desktop/College/fifith%20sem/Web%20technology/Fun/index2.html"
    )

    # 1. Enter book name
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[ng-model='bookname']")
        )
    ).send_keys("Java")

    # 2. Enter quantity
    driver.find_element(
        By.CSS_SELECTOR, "input[ng-model='quantity']"
    ).send_keys("5")

    # 3. Click Add
    driver.find_element(
        By.XPATH, "//button[normalize-space()='Add']"
    ).click()

    print("Add button test: PASS")

    # 4. Handle alert
    alert = wait.until(EC.alert_is_present())
    print("Alert message:", alert.text)
    alert.accept()

    print("Alert handled: PASS")

    # 5. Wait until the refreshed book list contains Java
    def book_is_displayed(d):
        items = d.find_elements(
            By.CSS_SELECTOR, "li[ng-repeat]"
        )
        return any(
            "Book Name: Java" in (item.text or "")
            for item in items
        )

    wait.until(book_is_displayed)

    # 6. Print current page text
    result = driver.find_element(By.TAG_NAME, "body").text
    print(result)
    print("Library test passed")

except Exception as e:
    print("Library test failed:", e)

finally:
    driver.quit()
