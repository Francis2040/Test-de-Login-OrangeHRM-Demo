import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.transfer_page import TransferPage

@pytest.fixture
def driver():
    # Inicializa Chrome con Service (Selenium 4.35+)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    driver.quit()

def test_transferencia(driver):
    # Login primero
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Ir a la página de transferencias
    transfer_page = TransferPage(driver)
    transfer_page.realizar_transferencia("Destinatario", 100)
    assert transfer_page.verificar_transferencia_exitosa()

