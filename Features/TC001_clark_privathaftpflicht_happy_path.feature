#This is a feature file which covers all the steps from launching Clarks stage URL till we see the offer on the app manager page

Feature: This feature covers the flow of Privathaftpflicht happy path for Basis plan

  Scenario: Privathaftpflicht Basis plan for the given details
    Given I launch the Clark application
    When   I click the Angebote link
    Then I expect to see the tile for Privathaftpflicht
    And I click on the tile Privathaftpflicht
    And I click on the Weiter button on Privathaftpflicht landing page
    And I select the radio button for Meine
    And I select the radio button for Ich bin im öffentlichen Dienst beschäftigt
    And I select the radio button for Gerne bin ich bereit bei einem Schaden bis zu 150,-EUR selbst zu zahlen, wenn dadurch meine Prämie sinkt
    And I enter "Test Comment" in the text box for Hast du noch weitere Informationen oder Anmerkungen für uns?
    And I click Angebot anfordem button
    And I expect to see the offer page Dein Angebot ist da!
    When I click on Zum Angebot button on Dein Angebot ist da page
    Then I expect to see the offers related to Privathpflicht
    When I click on Jetzt button on  Privathpflicht
    And I enter username and password details on registration page and click on registration button
    And I enter user details on Persönliche Angaben page and click on weiter button
    And I enter IBAN on Zahlungsdaten page and accept the terms and conditions
    And I click on tarif bestellen button
    And I click on Jetzt button on Angaben-Übersicht page
    Then I expect to see the confirmation page with the text Vielen Dank
    When I click on Zuruk zur button
    Then  I expect to see the offer on app manager page

