from datetime import datetime
from CLARK import configurationfile


class sicheredeinenfortschritt:

    email_input = (By.XPATH,"//div[contains(@class,'input')]/input[contains(@type,'email')]")
    password_input = (By.XPATH,"//div[contains(@class,'input')]/input[contains(@type,'password')]")
    submit_button = (By.XPATH,"//span[contains(@class,'content')]/span[contains(@class,'block')]")

    def fill_credentials(self):
        currTime = datetime.now()
        varEmailAddress = "testemail" + str(currTime.microsecond) + "@mailinator.com"
        varPassword = configurationfile.REGISTRATION_PASSWORD
        userEmail = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((sicheredeinenfortschritt.email_input)))
        userEmail.send_keys(varEmailAddress)
        userPassword = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((sicheredeinenfortschritt.password_input)))
        userPassword.send_keys(varPassword)
        button = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((sicheredeinenfortschritt.submit_button)))
        button.click()
