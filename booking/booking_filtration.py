# this will include a class with instance methods that will be responsible to interact
# with our website after we have some results,to apply filtration
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        
    def apply_star_rating(self, *star_values):
        start_filtration_box = self.driver.find_element_by_id('filter_class')
        start_child_elements = start_filtration_box.find_element_by_css_selector('*')
        print(len(start_child_elements))
        
        for star_value in star_values:
            for star_element in start_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value}stars':
                    star_element.click()

    def sort_price_lowest_first(self):
        element = self.driver.find_element_by_css_selector('li[data-i="price"]')
        element.click()