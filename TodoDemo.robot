*** Settings ***
Library  SeleniumLibrary
Library  ${EXECDIR}/Todo/TodoDemo.py

*** Test Cases ***
1 - Add Single todo into list
    [Documentation]  Ensure user able to land on todo apps and proceed to add todo into todo list
    ...  then verified todo is added successfully
    ...  Last Modified by Choon
    [Tags]   Todo        
    Given User Navigate to Todo Apps
    When User adds new Todo: TestingTodo
    Then validated todo: TestingTodo is added successfully

2- Add multiple todo into list and verify items count
    [Documentation]  Ensure user able add multiple todos and
    ...  then verify multiple todos is added successfully and count will increased accodingly
    ...  Last Modified by Choon
    [Tags]   Todo        
    Given User Navigate to Todo Apps
    When User adds new Todo: TestingTodo
    Then validated todo: TestingTodo is added successfully
    When User adds new Todo: TestingTodo2
    Then validated todo: TestingTodo2 is added successfully
    When User adds new Todo: TestingTodo3
    Then validated todo: TestingTodo3 is added successfully
    And verified items count: 3 is tally

3- Add multiple todo into list, perform and ensure able to check and uncheck then verify item count
    [Documentation]  Ensure user able add multiple todos and
    ...  perform check and uncheck action, when item is checked, count will decrease
    ...  when item being uncheck, count of item will be increase
    ...  Last Modified by Choon
    [Tags]   Todo        
    Given User Navigate to Todo Apps
    When User adds new Todo: TestingTodo
    And User adds new Todo: TestingTodo2
    And User adds new Todo: TestingTodo3
    Then verified item: TestingTodo2 can be checked
    And verified items count: 2 is tally
    Then verified item: TestingTodo2 can be unchecked
    And verified items count: 3 is tally


4- Not able to add todo when text length is less than 2
    [Documentation]  Ensure Minimum 2 character is need in order to add todo list
    ...  Last Modified by Choon
    [Tags]   Todo      
    Given User Navigate to Todo Apps
    When User adds new Todo: 1
    Then verified 0 item appear under All filter


5- Add multiple todo into list, and verify item will listed under active and completed filter correctly
    [Documentation]  Able to add multiple filter then perform check and verify item count again after checked
    ...  on both active and completed filter
    ...  Last Modified by Choon
    [Tags]   Todo        
    Given User Navigate to Todo Apps
    When User adds new Todo: TestingTodo
    And User adds new Todo: TestingTodo2
    And User adds new Todo: TestingTodo3
    Then verified item: TestingTodo2 can be checked
    And verified 2 item appear under Active filter
    And verified 1 item appear under Completed filter

6- Able to clear all completed filter
    [Documentation]  add multiple filter and checked, to mark item as completed, then proceed remove all
    ...   completed todo list
    ...   Last Modified by Choon
    [Tags]   Todo        
    Given User Navigate to Todo Apps
    When User adds new Todo: TestingTodo
    And User adds new Todo: TestingTodo2
    Then verified item: TestingTodo2 can be checked
    And verified item: TestingTodo can be checked
    And verified 2 item appear under Completed filter
    When User clears all completed todo list
    Then verified 0 item appear under All filter