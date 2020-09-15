from behave import*
from CLARK.pages.clark_sicheredeinenfortschritt_page import sicheredeinenfortschritt

obj = sicheredeinenfortschritt()

@when('I enter username and password details on registration page and click on registration button')
def fill_username_password(context):
    obj.fill_credentials()
