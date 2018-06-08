Feature: The calculator should be able to multiply numbers
    In order to make sure the calculator
    multiplies numbers correctly I have the following
    test scenarios:

    Scenario: My calculator can multiply
        Given I have the numbers 12 and 8
        When I multiply them
        Then I expect the result to be 96
