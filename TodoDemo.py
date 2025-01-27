from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

class TodoDemo(PageObject):

    @keyword('User Navigate to Todo Apps')
    def open_browser_to_todo_app(self):
        self.selib.open_browser('https://todomvc.com/examples/react/dist/', 'chrome')
        self.selib.maximize_browser_window()

    @keyword('User adds new Todo: ${todo}')
    def can_add_new_todo_items(self,new_todo):
        self.selib.input_text("//input[@class='new-todo']", new_todo)
        self.selib.press_keys("//input[@class='new-todo']", 'ENTER')  # Press Enter key

    @keyword('validated todo: ${todo} is added successfully')
    def validate_new_todo_item(self, new_item):
        todo_list = self.selib.get_webelement("(//ul[@class='todo-list']/li)[last()]")
        last_item = self.selib.get_text(todo_list)
        assert last_item == new_item, f"Expected '{new_item}', but found {last_item}"

    def can_filter_for_uncompleted_tasks(self):
        self.selib.click_element("//button[contains(text(),'Active')]")
        todo_list = self.selib.get_webelements("//ul[@class='todo-list']/li")
        assert len(todo_list) == 1, f"Expected 1 item, but found {len(todo_list)}"
        first_item = self.selib.get_text(todo_list[0])
        assert first_item == "Walk the dog", f"Expected 'Walk the dog', but found {first_item}"
        assert not self.selib.element_should_contain("//label[contains(text(),'Pay electric bill')]", "Pay electric bill")

    def can_filter_for_completed_tasks(self):
        self.selib.click_element("//button[contains(text(),'Completed')]")
        todo_list = self.selib.get_webelements("//ul[@class='todo-list']/li")
        assert len(todo_list) == 1, f"Expected 1 item, but found {len(todo_list)}"
        first_item = self.selib.get_text(todo_list[0])
        assert first_item == "Pay electric bill", f"Expected 'Pay electric bill', but found {first_item}"
        assert not self.selib.element_should_contain("//label[contains(text(),'Walk the dog')]", "Walk the dog")

    @keyword('user removes all completed task')
    def can_delete_all_completed_tasks(self):
        self.selib.click_element("//button[contains(text(),'Clear completed')]")
        todo_list = self.selib.get_webelements("//ul[@class='todo-list']/li")
        assert len(todo_list) == 1, f"Expected 1 item, but found {len(todo_list)}"
        first_item = self.selib.get_text(todo_list[0])
        assert first_item == "Walk the dog", f"Expected 'Walk the dog', but found {first_item}"
        assert not self.selib.element_should_contain("//label[contains(text(),'Pay electric bill')]", "Pay electric bill")
        assert not self.selib.is_element_visible("//button[contains(text(),'Clear completed')]")

    @keyword('verified item: ${todo} can be ${cond}')
    def can_check_off_an_item_as_completed(self, item, cond):
        self.selib.click_element("//label[contains(text(),'{0}')]/preceding::input[1]".format(item))
        todo_list_item = self.selib.get_webelement("//label[contains(text(),'{0}')]/ancestor::li".format(item))
        if cond =='checked':
            assert 'completed' in self.selib.get_element_attribute(todo_list_item, 'class')
        else:
            assert 'completed' not in self.selib.get_element_attribute(todo_list_item, 'class')


    @keyword('verified items count: ${num} is tally')
    def verify_item_count(self, num):
        todo_count = self.selib.get_webelements("//span[@class='todo-count']")
        todo_count = self.selib.get_text(todo_count)
        if 'items' in todo_count:
            count_str = '{0} items left!'.format(num)
        else:
            count_str = '{0} item left!'.format(num)
        assert count_str == todo_count, f"Expected '{count_str}', but found {todo_count}"

    @keyword('verified ${itemcount} item appear under ${filter} filter')
    def verify_item_count_under_filter(self, item_count, list_filter):
        if "All" not in list_filter:
            self.selib.click_element("//a[contains(text(),'{0}')]".format(list_filter))
        todo_list = self.selib.get_webelements("//ul[@class='todo-list']/li")
        assert len(todo_list) == int(item_count), f"Expected 0 item, but found {len(todo_list)}"

    @keyword('User clears all completed todo list')
    def remove_all_filter(self):
        self.selib.click_element("//button[contains(text(),'Clear completed')]")


    # def displays_two_todo_items_by_default(self):
    #     todo_list = self.selib.get_webelements("//ul[@class='todo-list']/li")
    #     assert len(todo_list) == 2, f"Expected 2 items, but found {len(todo_list)}"
    #     first_item = self.selib.get_text(todo_list[0])
    #     last_item = self.selib.get_text(todo_list[1])
    #     assert first_item == "Pay electric bill", f"Expected 'Pay electric bill', but found {first_item}"
    #     assert last_item == "Walk the dog", f"Expected 'Walk the dog', but found {last_item}"
    #
    # @keyword('User adds new todo ${todo}')
    # def can_add_new_todo_items(self, new_item):
    #     self.selib.input_text("//input[@class='new-todo']", new_item)
    #     self.selib.press_keys("//input[@data-test='new-todo']", '\u000D')  # Press Enter key
    #     # todo_list = self.selib.get_webelements("//ul[@class='todo-list']/li")
    #     # assert len(todo_list) == 3, f"Expected 3 items, but found {len(todo_list)}"
    #     # last_item = self.selib.get_text(todo_list[2])
    #     # assert last_item == new_item, f"Expected '{new_item}', but found {last_item}"
    #
    # @keyword('validated todo is added successfully')
    # def can_add_new_todo_items(self, new_item):
    #     todo_list = self.selib.get_webelement("(//ul[@class='todo-list']/li)[last()]")
    #     last_item = self.selib.get_text(todo_list)
    #     assert last_item == new_item, f"Expected '{new_item}', but found {last_item}"
    #
    # def can_check_off_an_item_as_completed(self):
    #     self.selib.click_element("//label[contains(text(),'Pay electric bill')]")
    #     self.selib.click_element("//input[@type='checkbox']")
    #     todo_list_item = self.selib.get_webelement("//label[contains(text(),'Pay electric bill')]/ancestor::li")
    #     assert 'completed' in self.selib.get_element_attribute(todo_list_item, 'class')
    #
    #

