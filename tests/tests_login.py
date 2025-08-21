import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    time.sleep(5)  # espera 5 segundos antes de cerrar
    driver.quit()

def test_login_correcto(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    dashboard = DashboardPage(driver)  # usa la clase importada
    assert dashboard.esta_visible()
    assert "dashboard" in driver.current_url.lower()