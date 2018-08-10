Feature: test for the lower-upper convent
  Scenario Outline: convent lower to upper
        When I open page
        When I input "<input_value>"
        When I click "<convent_type>"
        Then I see "<convent_result>"

     Examples: all request type
        |input_value|convent_type|convent_result|
        |abcdefghijklmn|大写|ABCDEFGHIJKLMN|
        |ABCDEFGHIJKLMN|小写|abcdefghijklmn|
        |ABCDEFGHIJKLMN|大写|ABCDEFGHIJKLMN|
        |abcdefghijklmn|大写|ABCDEFGHIJKLMn|
        |ABCDEFGHIJKLMN|小写|abcdefghijklmN|
        |ABCDEFGHIJKLMN|大写|ABCDEFGHIJKLMn|