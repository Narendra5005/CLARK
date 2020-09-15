from CLARK import configurationfile


class PersönlicheAngaben():

    herr = (By.XPATH,"(//span[contains(@class,'_label_9kmzts')])[1]")
    firstName = (By.XPATH,"//input[contains(@class,'first-name')]")
    lastName = (By.XPATH,"//input[contains(@class,'last-name')]")
    dateOfBirth = (By.XPATH,"//input[contains(@class,'birth-date')]")
    streetName = (By.XPATH,"//input[contains(@class,'street-name')]")
    houseNumber = (By.XPATH,"//input[contains(@class,'house-number')]")
    postalCode = (By.XPATH,"//input[contains(@class,'post-code')]")
    cityName = (By.XPATH,"//input[contains(@class,'city-name')]")
    phoneNumber = (By.XPATH,"//input[contains(@class,'phone-number')]")
    nextButton = (By.XPATH,"//span[text()='Weiter' and @class='_block_dsfphm']")

    def fill_details(self):
        option = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((PersönlicheAngaben.herr)))
        option.click()

        first_name = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((PersönlicheAngaben.firstName)))
        first_name.send_keys(configurationfile.REGISTRATION_FIRST_NAME)

        last_name = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((PersönlicheAngaben.lastName)))
        last_name.send_keys(configurationfile.REGISTRATION_LAST_NAME)

        dob = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((PersönlicheAngaben.dateOfBirth)))
        dob.send_keys(configurationfile.REGISTRATION_DOB)

        street = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((PersönlicheAngaben.streetName)))
        street.send_keys(configurationfile.REGISTRATION_STREET)

        house = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((PersönlicheAngaben.houseNumber)))
        house.send_keys(configurationfile.REGISTRATION_HOUSE)

        postal = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((PersönlicheAngaben.postalCode)))
        postal.send_keys(configurationfile.REGISTRATION_POSTAL)

        city = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((PersönlicheAngaben.cityName)))
        city.send_keys(configurationfile.REGISTRATION_CITY)

        phone = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((PersönlicheAngaben.phoneNumber)))
        phone.send_keys(configurationfile.REGISTRATION_PHONE)

        button = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((PersönlicheAngaben.nextButton)))
        button.click()








