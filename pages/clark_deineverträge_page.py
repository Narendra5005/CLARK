from CLARK.utils import  *

class deineverträge():

    jetzt_button = (By.XPATH,"(//button)[1]")
    privateOffersTile = (By.XPATH,"//*[contains(@class,'_title_2yb545')]")
    offer_element = (By.XPATH,"//*[contains(@class,'_title_niboal')]")

    def verify_offers(self):
        offer_text = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((deineverträge.privateOffersTile)))
        el_text = offer_text.text.replace("-","").replace("\xad","")
        print(el_text)
        if "Privathaftpflicht" not in el_text:
            print(el_text)
            raise Exception("Offer text is not displayed.")

    def click_jetzt_button(self):
        button = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((deineverträge.jetzt_button)))
        driver.execute_script("arguments[0].click();", button)

    def verify_offer_confirmation(self):
        offer_text = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((deineverträge.offer_element)))
        offer_str = offer_text.text
        if "Privathaftpflicht" not in offer_str:
            print(offer_text)
            raise Exception("Offer is not displayed.")
        driver.quit()


