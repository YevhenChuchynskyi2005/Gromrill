from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    MY_INFO_BUTTON = ("xpath", "//a[@class ='oxd-main-menu-item active']")

    def my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()