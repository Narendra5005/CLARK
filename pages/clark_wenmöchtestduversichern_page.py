from CLARK.utils import *

class wemochtestduversichern():
    MEINE_RADIO_BUTTON = (By.XPATH, "//li[contains(@class,'qu')]//div[contains(@class, 'questionnaire')]//input[contains(@value, 'Meine')]/..")
    #MEINE_RADIO_BUTTON_XPATH = "//li[contains(@class,'qu')]//div[contains(@class, 'questionnaire')]//input[contains(@value, 'Meine')]/.."
    def click_meine_radio(self):
        RADIO1 = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((wemochtestduversichern.MEINE_RADIO_BUTTON)))
        RADIO1.click()
        #driver.implicitly_wait(10)
        #driver.execute_script("arguments[0].click();", wemochtestduversichern.MEINE_RADIO_BUTTON_XPATH)
