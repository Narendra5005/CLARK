from behave import*
from CLARK.pages.clark_angebote_page import AngebotePage

obj = AngebotePage()

@then('I expect to see the tile for Privathaftpflicht')
def verify_tile(context):
     obj.verify_tile_isdisplyed()

@then('I click on the tile Privathaftpflicht')
def clickOnPrivathaftpflichtTile(context):
     obj.click_privathaftpflicht_tile()


