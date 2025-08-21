from selenium.webdriver.common.by import By

class TransferPage:
    def __init__(self, driver):
        self.driver = driver
        # Demo: solo simulación
        self.from_account = (By.ID, "fromAccount")
        self.to_account = (By.ID, "toAccount")
        self.amount_input = (By.ID, "amount")
        self.submit_button = (By.ID, "transferBtn")

    def make_transfer(self, from_acc, to_acc, amount):
        # Demo: simulación
        print(f"Transferencia simulada: {from_acc} -> {to_acc}, Monto: {amount}")
        return True
