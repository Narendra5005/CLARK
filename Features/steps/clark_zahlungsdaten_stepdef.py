from behave import*
from CLARK.pages.clark_zahlungsdaten_page import zahlungsdaten

obj = zahlungsdaten()

@when('I enter IBAN on Zahlungsdaten page and accept the terms and conditions')
def fill_iban_no(context):
    obj.fill_iban()

@when('I click on tarif bestellen button')
def click_tarif_btn(context):
    obj.click_tarif_button()
