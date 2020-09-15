from CLARK import configurationfile

wait = configurationfile.waitTime

class angabenubersicht():

    jetzt_button = (By.XPATH,"(//button[contains(@class,'mobile-block')])[2]")

    def click_jetzt_button(self):
        jetztBtn = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((angabenubersicht.jetzt_button)))
        jetztBtn.click()

