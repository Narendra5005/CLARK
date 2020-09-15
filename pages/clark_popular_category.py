from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CLARK.pages.Base import driver
from time import sleep


class clark_popular_category:
    wait = WebDriverWait(driver, 30)

    weitherButton = "//*[contains(@href,'offers/request')]"
    radioButtonMeine = (By.XPATH, "//li[contains(@class,'qu')]//div[contains(@class, 'questionnaire')]//input[contains(@value, 'Meine')]")

    def clickWeiterButton(self):
        weiter_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.weitherButton)))
        driver.execute_script("arguments[0].click();", weiter_button)


    def clickMeineRadioButton(self):
        radio1 = self.wait.until(EC.element_to_be_clickable(self.radioButtonMeine))
        driver.execute_script("arguments[0].click();", radio1)
        sleep(5)
        print("Quitting from life :P")
        driver.quit()

