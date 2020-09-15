from behave import*
from CLARK.pages.clark_angabenubersicht_page import angabenubersicht
obj = angabenubersicht()
@when('I click on Jetzt button on Angaben-Übersicht page')
def click_jetzt_btn(context):
    obj.click_jetzt_button()