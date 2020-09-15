from CLARK.utils import*

class LaunchClarkPage():

    angebote_link = (By.XPATH, "//*[contains(@href,'offers/request')]")
    private_offer_tile = (By.XPATH, "//*[contains(@href,'offers/request')]")

    def click_angebote_link(self):
        angeboteLink = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((LaunchClarkPage.angebote_link)))
        angeboteLink.click()

    def check_if_private_offers_tile_is_visible(self):
        private_offer = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((LaunchClarkPage.private_offer_tile)))
        if private_offer == True:
            print("Element is visible")
