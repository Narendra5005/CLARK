from CLARK.utils import *

class LaunchClarkPage():

    angeboteLink_xpath = "//*[contains(@href,'offers/request')]"
    privateOffersTile = "//*[contains(@title,'Privathaftpflicht')]"

    def click_angebote_link(self):
        angeboteLink = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((By.XPATH,LaunchClarkPage.angebote_link_locator)))
        angeboteLink.click()

    def check_if_private_offers_tile_is_visible(self):
        private_offer = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((By.XPATH,LaunchClarkPage.private_offers_tile_locator)))
        if private_offer == True:
            print("Element is visible")
