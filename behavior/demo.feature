Feature: test for the lower-upper convent
  Scenario: convent lower to upper
    When I open page
    When I input "abcdefghijk"
    When I click "大写"
    Then I see "ABCDEFGHIJK"

  Scenario: convent upper to lower
    When I open page
    When I input "ABCDEFGHIJK"
    When I click "小写"
    Then I see "abcdefghijk"

  Scenario: convent upper to lower
    When I open page
    When I input "ABCDEFghijk123"
    When I click "小写"
    Then I see "abcdefGHIJK123"