from behave import*
from CLARK.pages.clark_deinangebotistda_page import deinangebotistda

obj = deinangebotistda()

@then('I expect to see the offer page Dein Angebot ist da!')
def verify_offer_page(context):
    obj.verify_dein_angebot_offerpage()

@when('I click on Zum Angebot button on Dein Angebot ist da page')
def click_zum_button(context):
    obj.click_zum_btn()
