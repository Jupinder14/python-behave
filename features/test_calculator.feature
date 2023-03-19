Feature: Carbohydrate calculator

    Scenario: Test list_users api endpoint returns correct results
        Given I am on carbohydrate calculator page
        When I enter 28 in age
        And I select gender male
        And I enter 200 in height
        And I enter 85 in weight
        And I select moderate exercise
        And I click calculate
        Then I see results
        And I verify results are accurate
