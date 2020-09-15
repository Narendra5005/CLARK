from CLARK.utils import *

class deinangebotistda:

    zumAngebot = "//a[contains(@class, 'ember-view _button')]"
    zumButton = (By.XPATH,"//a[contains(@class, 'ember-view _button')]")

    def verify_dein_angebot_offerpage(self):
        is_offer_displayed = driver.find_elements(By.XPATH,deinangebotistda.zumAngebot)
        if(len(is_offer_displayed)==0):
            raise Exception("Offer page is not displayed.")

    def click_zum_btn(self):
        zumbtn = WebDriverWait(driver, wait).until(
            EC.element_to_be_clickable((deinangebotistda.zumButton)))
        zumbtn.click()
