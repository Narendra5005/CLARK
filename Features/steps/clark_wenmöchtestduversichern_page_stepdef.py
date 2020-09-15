from behave import*
from CLARK.pages.clark_wenmöchtestduversichern_page import wemochtestduversichern

obj = wemochtestduversichern

@then('I select the radio button for Meine')
def click_radio_button(context):
    obj.click_meine_radio(context)

