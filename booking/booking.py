# import constants as const
from selenium import webdriver
import os
from booking_filtration import BookingFiltration
from booking_report import BookingReport
from prettytable import PrettyTable
driver = webdriver.Chrome("C:/Users/LENOVO pc/SeleniumDrivers/chromedriver")


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/Users/LENOVO pc/SeleniumDrivers/chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get("https://www.booking.com")
        # self.get(BASE_URL)
            
    def change_currency(self, currency):
        currency_element = self.find_element_by_css_selector('button[data-tooltip-text = "Choose your currency"]')
        currency_element.click()
            
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()
            
    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element_by_css_selector('li[data-i="0"]')
        first_result.click()
            
    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(f'td[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element_by_css_selector(f'td[data-date = "{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        select_element = self.find_element_by_id('xp__guests__toggle')
        select_element.click()
                                                                
        while True:
            decrease_adults_element = self.find_element_by_css_selector('button[aria-label="Decrease number of Adults"]')
            decrease_adults_element.click()
            # ----if the value of adults reaches 1, then we should get out of the while loop
            adults_value_element = self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute('value')
            # ---should give back the adults count
            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element_by_css_selector('button[ aria-label="Increase number of Adults"]')
        for _ in range(count - 1):
            increase_button_element.click()
                                                                
    def click_search(self):
        search_button = self.find_element_by_css_selector('button[type="Submit"]')
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(4, 5)
        filtration.sort_price_lowest_first()

    def report_results(self):
        hotel_boxes = self.find_element_by_id('hotellist_inner')
        # find_element_by_class_name('sr_property_block')
        # return hotel_boxes
        report = BookingReport(hotel_boxes)
        # report.display_table()
        report.pull_titles()
        table = PrettyTable(field_names=["Hotel Name", "Hotel Price", "Hotel Score"])
        table.add_rows(report.pull_deal_box_attributes())
        # print(report.pull_deal_box_attributes())
        print(table)