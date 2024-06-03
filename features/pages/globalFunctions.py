import secrets
import string
import time

from faker import Faker
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

faker = Faker()


class BaseFunctions:
    def __init__(self, driver):
        self.driver = driver

    def defined_waiting_time(self, tie):
        time.sleep(tie)

    def navigate(self, url, tie):
        self.driver.get(url)
        self.driver.maximize_window()
        print(f"Opened page: {url}")
        self.defined_waiting_time(tie)

    def select_element(self, by, selector, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return element
        except TimeoutException as ex:
            print(f"Timeout: Element {selector} not found. {ex}")
            return None

    def mixed_text(self, by, selector, text, tie):
        element = self.select_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element:
            element.clear()
            element.send_keys(text)
            print(f"Writing the text '{text}' in the field {selector}")
        self.defined_waiting_time(tie)

    def mixed_click(self, by, selector, tie):
        element = self.select_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element:
            element.click()
            print(f"Clicked on the field {selector}")
        self.defined_waiting_time(tie)

    def select_by_type(self, by, selector, select_by, value, tie):
        element = self.select_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element:
            select = Select(element)
            if select_by == "text":
                select.select_by_visible_text(value)
            elif select_by == "index":
                select.select_by_index(value)
            elif select_by == "value":
                select.select_by_value(value)
            print(f"Selected {value} in the field {selector}")
        self.defined_waiting_time(tie)

    def multiple_upload(self, by, selector, file_path, tie):
        element = self.select_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element:
            element.send_keys(file_path)
            print(f"The file is loaded with the path: {file_path}")
        self.defined_waiting_time(tie)

    def check_element(self, by, selector, tie):
        self.mixed_click(by, selector, tie)

    def check_multiple_elements(self, tie, *selectors):
        for selector in selectors:
            self.check_element(By.XPATH, selector, tie)

    def validate_if_exists(self, by, selector, tie):
        element = self.select_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.defined_waiting_time(tie)
        if element:
            print(f"The element {selector} --> Exists")
            return "Exists"
        else:
            print(f"The element {selector} --> Does not exist")
            return "Does not exist"

    def perform_action(self, by, selector, action, tie):
        element = self.select_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element:
            actions = ActionChains(self.driver)
            if action == "double_click":
                actions.double_click(element).perform()
            elif action == "right_click":
                actions.context_click(element).perform()
            print(f"{action.replace('_', ' ').capitalize()} on {selector}")
        self.defined_waiting_time(tie)

    def drag_and_drop(self, by, source_selector, dest_selector, tie):
        source_element = self.select_element(by, source_selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", source_element)
        dest_element = self.select_element(by, dest_selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", dest_element)
        if source_element and dest_element:
            actions = ActionChains(self.driver)
            actions.drag_and_drop(source_element, dest_element).perform()
            print(f"Dragged {source_selector} to {dest_selector}")
        self.defined_waiting_time(tie)

    def drag_and_drop_by_offset(self, by, selector, x, y, tie=0.2):
        element = self.select_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        if element:
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(element, x, y).perform()
            print(f"Dragged {selector} by offset ({x}, {y})")
        self.defined_waiting_time(tie)

    def click_by_offset(self, by, selector, x, y, tie):
        element = self.select_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element:
            actions = ActionChains(self.driver)
            actions.move_to_element_with_offset(element, x, y).click().perform()
            print(f"Clicked on {selector} at offset ({x}, {y})")
        self.defined_waiting_time(tie)

    def generate_random_password(self, length=12):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    def generate_random_email(self):
        return faker.email()

    def generate_random_name(self):
        return faker.first_name()

    def generate_random_last_name(self):
        return faker.last_name()

    def exit(self):
        print("The test ended successfully")
