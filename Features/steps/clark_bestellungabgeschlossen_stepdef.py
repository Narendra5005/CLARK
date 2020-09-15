from behave import*
from CLARK.pages.clark_bestellungabgeschlossen_page import bestellungabgeschlossen

obj = bestellungabgeschlossen()

@then('I expect to see the confirmation page with the text Vielen Dank')
def verify_conf_page(context):
    obj.verify_confirmation_page()

@when('I click on Zuruk zur button')
def click_zuruck_btn(context):
    obj.click_zuruck_button()
