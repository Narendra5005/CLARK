from CLARK.utils import *

class bestellungabgeschlossen:

    confirmation = "//*[contains(text(),'Vielen Dank')]"
    zuruck_button = (By.XPATH,"//button")
    close_btn_popup = (By.XPATH,"//button[contains(@class,'close')]")

    def verify_confirmation_page(self):
        is_offer_displayed = driver.find_elements(By.XPATH, bestellungabgeschlossen.confirmation)
        if (len(is_offer_displayed) == 0):
            raise Exception("Confirmation page is not displayed.")

    def click_zuruck_button(self):
        button = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((bestellungabgeschlossen.zuruck_button)))
        button.click()
        close_popup = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((bestellungabgeschlossen.close_btn_popup)))
        close_popup.click()
