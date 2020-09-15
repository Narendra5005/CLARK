from CLARK.utils import *
from CLARK.pages.clark_basePage import driver

class AngebotePage():

    PRIVATE_OFFER_TILE = (By.XPATH, "//*[contains(@title,'Privathaftpflicht')]")
    offer_tile = "//*[contains(@title,'Privathaftpflicht')]"

    def verify_tile_isdisplyed(self):
        is_tile_displayed = driver.find_elements(By.XPATH, AngebotePage.offer_tile)
        if (len(is_tile_displayed) == 0):
            raise Exception("Tile is not displayed.")

    def click_privathaftpflicht_tile(self):
        WebDriverWait(driver, wait).until(EC.element_to_be_clickable((AngebotePage.PRIVATE_OFFER_TILE))).click()
