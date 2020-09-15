from CLARK.utils import *

class möchtestdubeieinemschadensfall:
    gerneBinRadio = (By.XPATH,"//*[contains(@id,'Gerne bin')]/..")

    def click_gerne_bin(self):
        gerneRadioButton = WebDriverWait(driver, wait).until(
            EC.element_to_be_clickable((möchtestdubeieinemschadensfall.gerneBinRadio)))
        gerneRadioButton.click()