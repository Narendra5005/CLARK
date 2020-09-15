from CLARK import configurationfile


class zahlungsdaten:

    iban_input = (By.XPATH,"//input[contains(@class,'iban-offer')]")
    termsAndConditionsCheckBox = (By.XPATH,"//span[contains(@class,'custom-checkbox')]")
    tarifButton = (By.XPATH,"//button[contains(@class,'next-split')]")

    def fill_iban(self):
        iban = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((zahlungsdaten.iban_input)))
        iban.send_keys(configurationfile.IBAN)
        checkbox = WebDriverWait(driver, wait).until(EC.visibility_of_element_located((zahlungsdaten.termsAndConditionsCheckBox)))
        driver.execute_script("arguments[0].click();", checkbox)

    def click_tarif_button(self):
        button = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((zahlungsdaten.tarifButton)))
        button.click()
