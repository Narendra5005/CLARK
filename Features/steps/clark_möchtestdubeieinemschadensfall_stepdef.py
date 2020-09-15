from behave import*
from CLARK.pages.clark_möchtestdubeieinemschadensfall_page import möchtestdubeieinemschadensfall

obj = möchtestdubeieinemschadensfall()

@then('I select the radio button for Gerne bin ich bereit bei einem Schaden bis zu 150,-EUR selbst zu zahlen, wenn dadurch meine Prämie sinkt')
def click_gerne_bin_button(context):
    obj.click_gerne_bin()