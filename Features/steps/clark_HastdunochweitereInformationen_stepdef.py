from behave import*
from CLARK.pages.clark_HastdunochweitereInformationen_page import HastdunochweitereInformationen

obj = HastdunochweitereInformationen()

@then('I enter "Test Comment" in the text box for Hast du noch weitere Informationen oder Anmerkungen für uns?')
def enter_test_comment(context):
    obj.fill_test_comment()

@then('I click Angebot anfordem button')
def click_angebot(context):
    obj.click_angebot_button();