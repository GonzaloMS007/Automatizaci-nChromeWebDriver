import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def chrome():
    opciones = webdriver.ChromeOptions()
    opciones.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    driver = webdriver.Chrome(options=opciones)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_cliente(chrome):
    chrome.get("https://www.google.com")
    chrome.maximize_window()

    search_box = chrome.find_element(By.NAME, "q")
    search_box.send_keys("chalito_ms TIKTOK")
    search_box.submit()
    time.sleep(2)

    chrome.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a/h3').click()
    time.sleep(5)

if __name__ == "__main__":
    pytest.main()
