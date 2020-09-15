from CLARK.utils import *

class triffteinerderaufgeführten:
    radioButtonForIchBinImOffentlichen = (By.XPATH,"//input[contains(@value, 'Ich bin im')]/../..")
    weiterButton = (By.XPATH,"//button[contains(@class,'next')]")

    def click_Ichbin_radio_button(self):
        ichbinRadioButton = WebDriverWait(driver, wait).until(
            EC.element_to_be_clickable((triffteinerderaufgeführten.radioButtonForIchBinImOffentlichen)))
        driver.execute_script("arguments[0].click();", ichbinRadioButton)
