from behave import*
from CLARK.pages.clark_triffteinerderaufgeführten_page import triffteinerderaufgeführten

obj = triffteinerderaufgeführten()

@then('I select the radio button for Ich bin im öffentlichen Dienst beschäftigt')
def click_Ich_bin_radio_button(context):
    obj.click_Ichbin_radio_button()