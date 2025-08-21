import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    driver.quit()

def test_ver_dashboard(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    dashboard = DashboardPage(driver)
    header = dashboard.get_dashboard_header()
    assert "dashboard" in header.lower()
