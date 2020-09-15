from CLARK.utils import *

class HastdunochweitereInformationen:

    textBoxToEnterInfo = (By.XPATH,"//input[contains(@class,'text-field-answer')]")
    angeboteAnfordernButton = (By.XPATH,"//button[contains(@class, 'btn-next-split')]")

    def fill_test_comment(self):
        inputTextbox = WebDriverWait(driver, wait).until(
            EC.visibility_of_element_located((HastdunochweitereInformationen.textBoxToEnterInfo)))
        inputTextbox.send_keys("Test Comment")

    def click_angebot_button(self):
        anfordernBtn = WebDriverWait(driver, wait).until(
            EC.element_to_be_clickable((HastdunochweitereInformationen.angeboteAnfordernButton)))
        anfordernBtn.click()
