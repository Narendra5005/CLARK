from behave import*
from CLARK.pages.clark_deineverträge_page import deineverträge

obj = deineverträge()

@then('I expect to see the offers related to Privathpflicht')
def verify_offer_page(context):
    obj.verify_offers()

@when('I click on Jetzt button on  Privathpflicht')
def click_jetzt_btn(context):
    obj.click_jetzt_button()

@then('I expect to see the offer on app manager page')
def verify_offer_conf(context):
    obj.verify_offer_confirmation()