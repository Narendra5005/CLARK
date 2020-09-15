from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from CLARK.pages.clark_basePage import driver
from CLARK import configurationfile

wait = configurationfile.waitTime

class PrivathaftpflichtPage():
    WEITER_BUTTON = (By.XPATH, "//button[contains(@class,'continue')]")

    def click_weiter_button(self):
        weiterButton = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((PrivathaftpflichtPage.WEITER_BUTTON)))
        weiterButton.click()






