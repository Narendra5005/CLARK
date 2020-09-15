from behave import*
from CLARK.pages.clark_privathaftpflicht_page import PrivathaftpflichtPage

obj = PrivathaftpflichtPage()

@then('I click on the Weiter button on Privathaftpflicht landing page')
def clickWeiterButton(context):
    obj.click_weiter_button()
