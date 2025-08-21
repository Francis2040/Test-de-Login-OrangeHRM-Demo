from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        # Ajusta el selector según lo que inspecciones
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")

    def esta_visible(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.dashboard_header)
        )
        return True
