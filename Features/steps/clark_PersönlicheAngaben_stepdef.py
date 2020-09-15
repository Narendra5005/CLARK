from behave import*
from CLARK.pages.clark_PersönlicheAngaben import PersönlicheAngaben

obj = PersönlicheAngaben()

@when('I enter user details on Persönliche Angaben page and click on weiter button')
def fill_user_details(context):
    obj.fill_details()
