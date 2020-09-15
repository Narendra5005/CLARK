from behave import*
from CLARK.pages.clark_basePage import Base

obj = Base()

from CLARK.pages.clark_landing_page import LaunchClarkPage
objLaunch = LaunchClarkPage

@given('I launch the Clark application')
def launchClarkApplication(context):
    obj.launchClarkPage()

@when('I click the Angebote link')
def clickAngeboteLink(context):
     objLaunch.click_angebote_link(context)

